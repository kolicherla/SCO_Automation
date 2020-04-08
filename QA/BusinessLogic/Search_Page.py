from QA.Utilities.PerformAction import PerformActions
from QA.PageObjects.Test_Locators import PCN
from QA.Utilities.CommonLib import CommonFunctions
from QA.Base.Config import MyConfigFiles
from QA.BusinessLogic.Home_Page import Home
from QA.BusinessLogic.Filter_Page import Filter
from QA.BusinessLogic.CreateJPCN_Page import createJPCN_Page
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
from pathlib import Path
from selenium import webdriver
import sys
import datetime
from pytz import timezone
import time

class Search_Page():
    global objCommon, objActions ,objConfig,objFilter,objHome,objCreateJPCN
    objCommon = CommonFunctions()
    objActions = PerformActions()
    objConfig=MyConfigFiles()
    objFilter=Filter()
    objHome=Home()
    objCreateJPCN = createJPCN_Page()

    def Select_ResponsibleContextCE(self, strResponsibleCoreCE):
        objActions.selectDropdown(PCN.Validate_ResponsibleCE_Value_name, "name", "visibletext", strResponsibleCoreCE)
        print("Successfully selected" + strResponsibleCoreCE)
        time.sleep(5)

    def Click_Search_Button(self):
        objActions.clickElement(PCN.Search_Button_xpath, "xpath")
        print("Clicked Search Button")
        time.sleep(5)

    # def Click_Dashboard(self):
    #     objActions.clickElement("//a[@class='active']", "xpath")
    #     objActions.clickElement("//a[contains(text(),'Dashboard')]", "xpath")
    #     JPCNstatusoverview_Page.ClickContextCE_Create_Items(self)
    #     # objActions.clickElement("//body/div[@id='root']/div/main[@class='main-page']/div[@class='content']/main/span[@class='content']/div[@class='tiles padding-left']/div[1]/div[1]","xpath")
    #     objActions.clickElement("//td[text()='JPCN-100100663']", "xpath")
    #     time.sleep(5)

    def GetCoreCENames(self):
        objTablerow = MyConfigFiles.driver.find_elements_by_xpath("//table[@id='upload-jpn']/tbody/tr")
        intRowCount = len(objTablerow)
        print(intRowCount)
        strCoreCEList1 = []
        for strCoreCEList in MyConfigFiles.driver.find_elements_by_xpath("//table[@id='upload-jpn']/tbody/tr/td[14]"):
            strCoreCEList1.append(strCoreCEList.text)
            print(strCoreCEList.text)
        print(strCoreCEList1)
        CoreCESet = set(strCoreCEList1)
        CoreCEList = list(CoreCESet)
        print(CoreCEList)
        CoreCENames = len(CoreCEList)
        print(CoreCENames)
        CoreCount = 0
        for x in CoreCEList:
            CoreCount1 = CoreCount
            CoreCount=0
            CoreCount = strCoreCEList1.count(x)
            print(CoreCount)
            if CoreCount > CoreCount1:
                CoreCount1 = CoreCount
                print(x)

    def Verify_Search_Results_ResContextCEName(self,UserName):
        global CoreCEAssessment_JPCNNumber
        strPages = objActions.getText(PCN.Search_TablePage_Count_xpath, "xpath")
        strPagesCount = strPages.split(" ")
        PageCount = int(strPagesCount[4])
        print(PageCount)
        objTablerow = MyConfigFiles.driver.find_elements_by_xpath("//table[@id='created-jpcn']/tbody/tr")
        intRowCount = len(objTablerow)
        print("Rows Count in page  is: " + str(intRowCount - 1))
        flag = False
        for t in range(1, PageCount + 1):
            for i in range(2, intRowCount + 1):
                stri = str(i)
                strJCPNStage = objActions.getText("//table[@id='created-jpcn']/tbody/tr[" + stri + "]/td[13]", "xpath")
                if strJCPNStage == UserName:
                    print("Expected results is:"+strJCPNStage + " ", "Actual results are same :" +UserName)
                else:
                    print("Searched Results are not matched")
                assert strJCPNStage == UserName
                break

    def Search_For_ClosedPCN_And_ClickEditIcon(self):
        global CoreCEAssessment_JPCNNumber
        strPages = objActions.getText(PCN.Search_TablePage_Count_xpath, "xpath")
        strPagesCount = strPages.split(" ")
        PageCount = int(strPagesCount[4])
        print(PageCount)
        objTablerow = MyConfigFiles.driver.find_elements_by_xpath("//table[@id='created-jpcn']/tbody/tr")
        intRowCount = len(objTablerow)
        print("Rows Count in page  is: " + str(intRowCount - 1))
        flag = False
        for t in range(1, PageCount + 1):
            for i in range(2, intRowCount + 1):
                stri = str(i)
                strJCPNStage = objActions.getText("//table[@id='created-jpcn']/tbody/tr[" + stri + "]/td[7]", "xpath")
                if strJCPNStage == "Core CE Assessment":
                    EditIconExists = objActions.ObjectExists( "//table[@id='created-jpcn']/tbody//tr[" + stri + "]//td[2]//img[@class='editIcon iconLink']", "xpath")
                    CoreCEAssessment_JPCNNumber = MyConfigFiles.driver.find_element_by_xpath("//table[@id='created-jpcn']/tbody//tr[" + stri + "]//td[3]").text
                    objActions.clickElement("//table[@id='created-jpcn']/tbody//tr[" + stri + "]//td[2]//img[@class='editIcon iconLink']", "xpath")
                    if EditIconExists == True:
                        flag = True
                        print("Able to edit Closed JPCN")
                        break
            if flag == True:
                break
            elif t == PageCount:
                break
            else:
                time.sleep(2)
                objActions.clickElement("//a[text()='" + str(t + 1) + "']", "xpath")
                time.sleep(2)
        if flag == False:
            sys.exit("FAILED:: Could not find the JPCNNumber ")
        else:
            print("Core CE Assessment JPCN is " + CoreCEAssessment_JPCNNumber + "and successfully clicked edit icon")
        return CoreCEAssessment_JPCNNumber


    def Edit_PCNPDN_BySearch(self,DescriptionChange,EditComments):
        objbefore_Edit = objCreateJPCN.get_EnterPCNDetails_all_data()
        objActions.clickElement(PCN.Expand_PCN_PDNInfo_Edit_Button_xpath, "xpath")
        objActions.enterText(PCN.Descriptionchange_WebEdit_name, "name", DescriptionChange)
        objActions.enterText(PCN.PCN_PDN_EditComments_WebEdit_name, "name", EditComments)
        time.sleep(2)
        html = MyConfigFiles.driver.find_element_by_tag_name('html')
        html.send_keys(Keys.PAGE_UP)
        objActions.clickElement(PCN.Expand_PCN_PDNInfo_Save_Button_xpath, "xpath")
        time.sleep(2)
        objAfter_Edit=objCreateJPCN.get_EnterPCNDetails_all_data()
        assert objbefore_Edit != objAfter_Edit

    def Search_For_ClosedPCN_And_ClickReOpenIcon(self):
        global Closed_JPCNNumber
        strPages = objActions.getText(PCN.Search_TablePage_Count_xpath, "xpath")
        strPagesCount = strPages.split(" ")
        PageCount = int(strPagesCount[4])
        print(PageCount)
        objTablerow = MyConfigFiles.driver.find_elements_by_xpath("//table[@id='created-jpcn']/tbody/tr")
        intRowCount = len(objTablerow)
        print("Rows Count in page  is: " + str(intRowCount - 1))
        flag = False
        for t in range(1, PageCount + 1):
            for i in range(2, intRowCount + 1):
                stri = str(i)
                strJCPNStage = objActions.getText("//table[@id='created-jpcn']/tbody/tr[" + stri + "]/td[7]", "xpath")
                if strJCPNStage == "PCN Closed":
                    # strJPCNID=objActions.getText("//table[@id='created-jpcn']/tbody/tr[" + stri + "]/td[3]", "xpath")
                    # print(strJPCNID)
                    reopenIconExists = objActions.ObjectExists( "//table[@id='created-jpcn']/tbody//tr[" + stri + "]//td[2]//img[@class='openIcon iconLink']", "xpath")
                    Closed_JPCNNumber = MyConfigFiles.driver.find_element_by_xpath("//table[@id='created-jpcn']/tbody//tr[" + stri + "]//td[3]").text
                    objActions.clickElement("//table[@id='created-jpcn']/tbody//tr[" + stri + "]//td[2]//img[@class='openIcon iconLink']", "xpath")
                    if reopenIconExists == True:
                        flag = True
                        print("Able to ReOpen Closed JPCN")
                        break
            if flag == True:
                break
            elif t == PageCount:
                break
            else:
                time.sleep(2)
                objActions.clickElement("//a[text()='" + str(t + 1) + "']", "xpath")
                time.sleep(2)
        if flag == False:
            sys.exit("FAILED:: Could not find the JPCNNumber ")
        else:
            print("Core CE Assessment JPCN is " + Closed_JPCNNumber + "and successfully clicked edit icon")
        return Closed_JPCNNumber

    def ReOpen_PCNPDN_BySearch(self):
        strReopen_Msg=objActions.getText(PCN.ReOpen_PopUP_Msg_WebElement_xpath, "xpath")
        print("Reopen the JPCN initiated:" +strReopen_Msg )
        time.sleep(2)
        objActions.clickElement(PCN.MultipleCoreCE_POpUp_Button_xpath, "xpath")
        objCommon.capture_screenshot("Sucessfully navigates to JPCN Status Overview Dashboard page")
        time.sleep(2)
        objActions.clickElement(PCN.DashBoard_InitialAssessment_WebElement_xpath, "xpath")
        time.sleep(2)


    def Search_For_ClosedPCN_And_ClickDuplicatingJPCNIcon(self):
        global JPCNNumber,objData1
        strPages = objActions.getText(PCN.Search_TablePage_Count_xpath, "xpath")
        strPagesCount = strPages.split(" ")
        PageCount = int(strPagesCount[4])
        print(PageCount)
        objTablerow = MyConfigFiles.driver.find_elements_by_xpath("//table[@id='created-jpcn']/tbody/tr")
        intRowCount = len(objTablerow)
        print("Rows Count in page  is: " + str(intRowCount - 1))
        flag = False
        for t in range(1, PageCount + 1):
            for i in range(2, intRowCount + 1):
                stri = str(i)
                strJCPNStage = objActions.getText("//table[@id='created-jpcn']/tbody/tr[" + stri + "]/td[7]", "xpath")
                if strJCPNStage == "Context CE - PCN Creation":
                    objActions.clickElement("//table[@id='created-jpcn']/tbody//tr[" + stri + "]//td[3]", "xpath")
                    time.sleep(2)
                    objActions.clickElement(PCN.Expand_SupplierInfo_Button_xpath, "xpath")
                    time.sleep(2)
                    objActions.clickElement(PCN.Expand_PCN_PDNinfo_Button_xpath, "xpath")
                    time.sleep(2)
                    objData1 = objCreateJPCN.get_EnterPCNDetails_all_data()
                    time.sleep(2)
                    objActions.clickElement(PCN.PCN_Details_Cancel_button_xpath, "xpath")
                    time.sleep(2)
                    DuplicateIconExists = objActions.ObjectExists( "//table[@id='created-jpcn']/tbody//tr[" + stri + "]//td[2]//img[@class='duplicateIcon iconLink']", "xpath")
                    JPCNNumber = MyConfigFiles.driver.find_element_by_xpath("//table[@id='created-jpcn']/tbody//tr[" + stri + "]//td[3]").text
                    objActions.clickElement("//table[@id='created-jpcn']/tbody//tr[" + stri + "]//td[2]//img[@class='duplicateIcon iconLink']", "xpath")
                    if DuplicateIconExists == True:
                        flag = True
                        print("Able to Duplicate Closed JPCN")
                        break
            if flag == True:
                break
            elif t == PageCount:
                break
            else:
                time.sleep(2)
                objActions.clickElement("//a[text()='" + str(t + 1) + "']", "xpath")
                time.sleep(2)
        if flag == False:
            sys.exit("FAILED:: Could not find the JPCNNumber ")
        else:
            print("Core CE Assessment JPCN is " + JPCNNumber + "and successfully clicked edit icon")
        return objData1

    def Duplicating_PCNPDN_BySearch(self):
        strReopen_Msg = objActions.getText(PCN.Duplicating_Msg_WebElement_xpath, "xpath")
        print("Duplicating the JPCN initiated:" + strReopen_Msg)
        time.sleep(2)
        objActions.clickElement(PCN.MultipleCoreCE_POpUp_Button_xpath, "xpath")
        Duplicate_JPCN=objActions.getText(PCN.Dupicating_JPCN_ID_WebElement_xpath, "xpath")
        JPCN_Number=Duplicate_JPCN.split(" ",1)[0]
        objCommon.capture_screenshot("Duplicated JPCN created Sucessfully" +JPCN_Number)
        print("Duplicating JPCN Nummber Created :" +JPCN_Number)
        time.sleep(2)
        objActions.clickElement(PCN.Duplicating_MsgBox_Close_xpath, "xpath")
        time.sleep(2)
        return JPCN_Number










