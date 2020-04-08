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

class ClosureAssessment_Page():
    global objCommon, objActions ,objConfig,objFilter,objHome,objCreateJPCN
    objCommon = CommonFunctions()
    objActions = PerformActions()
    objConfig=MyConfigFiles()
    objFilter=Filter()
    objHome=Home()
    objCreateJPCN = createJPCN_Page()


    def Closure_Assesement_DashBorad_Link(self):
        time.sleep(2)
        objActions.clickElement(PCN.DashBoard_ContextCE_ClosureAssessment_WebElement_xapth, "xpath")
        time.sleep(3)
        objCommon.capture_screenshot("Closure Assessment  Page intiiated")

    def ValidationcheckFor_JPNMPNInfor_Section(self):
        objCreateJPCN.ClickOnJPN_MPN_Exapnd()
        time.sleep(3)
        global flag
        time.sleep(2)
        strPages = objActions.getText(PCN.ContextCE_TablePage_Count_xpath, "xpath")
        strPagesCount = strPages.split(" ")
        intPagesCount = int(strPagesCount[4])
        flag = False
        for pages in range(1, intPagesCount + 1):
            objTable = MyConfigFiles.driver.find_elements_by_xpath("//table[@id='upload-jpn']/tbody/tr")
            intRowCount = len(objTable)
            for i in range(2, intRowCount + 1):
                stri = str(i)
                objTablecol = MyConfigFiles.driver.find_elements_by_xpath("//table[@id='upload-jpn']/tbody/tr/th")
                intColCount = len(objTablecol)
                for j in range(i, intColCount + 1):
                    strj = str(j)
                    strchoosefile = objActions.getText("//table[@id='upload-jpn']/tbody/tr[" + stri + "]/td[2]", "xpath")
                    if strchoosefile == "MAXIM":
                        time.sleep(2)
                        objActions.clickElement("//table[@id='upload-jpn']/tbody/tr[" + stri + "]/td[2]//a[1]", "xpath")
                        time.sleep(2)
                        LTB_Decision = MyConfigFiles.driver.find_element_by_xpath("//div[contains(@class,'supplier-info-section padding-around show-it')]//select[@id='selectDrpDwn']")
                        LTB_DStatus= LTB_Decision.is_enabled()
                        LTB_Comments = MyConfigFiles.driver.find_element_by_xpath("//tr[8]//td[2]//div[1]//div[1]//div[1]//input[1]")
                        LTB_CStatus=LTB_Comments.is_enabled()
                        if (LTB_DStatus) and  (LTB_CStatus) == True:
                            print("LTB Decision and Comments are  Editable")
                            objActions.selectDropdown("//div[contains(@class,'supplier-info-section padding-around show-it')]//select[@id='selectDrpDwn']", "xpath", "visibletext", "Bridge Buy")
                            time.sleep(3)
                            objActions.enterText("//tr[8]//td[2]//div[1]//div[1]//div[1]//input[1]", "xpath", "Comments")
                            time.sleep(3)
                            objCommon.capture_screenshot("LTB Decision and LTB comments sucessfully edited and saved" )
                            objActions.clickElement(PCN.Submit_SR_button_xpath, "xpath")
                            time.sleep(3)
                        else:
                            print("LTB Decision and Comments are not Editable")
                            objCommon.capture_screenshot("LTB Decision and Comments are not Editable")
                            time.sleep(3)
                            objActions.clickElement(PCN.Cancel_Button_xpath, "xpath")
                            flag =True
                            break

    def ValidationcheckFor_CONTEXTCE_DETAILS_Section_ClosureAssessment(self,PCNStatus):
        time.sleep(2)
        objActions.selectDropdown(PCN.Validate_PCNStatus_Value_name, "name", "visibletext", PCNStatus)
        html = MyConfigFiles.driver.find_element_by_tag_name('html')
        html.send_keys(Keys.TAB)
        time.sleep(2)
        strIPCNS_Act = objActions.getText(PCN.Validation_msg_ClosureAssesment_WebElement_xapth, "xpath")
        time.sleep(2)
        strIPCNS_Exp = "Invalid pcn status"
        if strIPCNS_Act == strIPCNS_Exp:
            print("Passed - Validation Message is dispalying as::"  " " + strIPCNS_Act)
        else:
            print("Failed -NO validation message is displayed")
        assert strIPCNS_Act == strIPCNS_Exp

    def Fill_CONTEXTCE_Drtails_Section_ClosureAssessment(self, PCNStatus,pcnComments,pcnClosedComments):
        time.sleep(2)
        objActions.selectDropdown(PCN.Validate_PCNStatus_Value_name, "name", "visibletext", PCNStatus)
        time.sleep(3)
        objActions.enterText(PCN.Validate_PCNStatusComment_Value_name, "name", pcnComments)
        time.sleep(3)
        objActions.enterText(PCN.PCNStatusClose_Comments_name, "name", pcnClosedComments)
        time.sleep(3)
        objActions.clickElement(PCN.Close_Assessment_WebElement_xpath, "xpath")
        # Waring_Msg=objActions.getText(PCN.Close_Assessment_Warning_WebElement_xpath, "xpath")
        # print(Waring_Msg)
        # assert (objActions.AssertObjectExists(PCN.Close_Assessment_Warning_WebElement_xpath, "xpath"))



    def EDit_PR_Section_ClosureAssessment(self,PCNStatus,pcnComments,pcnClosedComments):
        time.sleep(3)
        global flag
        time.sleep(4)
        objTable = MyConfigFiles.driver.find_elements_by_xpath("//div[@class='context-ce-details-section padding-around show-it']//div[@class='inline']//div//table[@id='pr']/tbody/tr")
        intRowCount = len(objTable)
        for i in range(2, intRowCount + 1):
            stri = str(i)
            strEcoMcoStatus = objActions.getText("//div[@class='context-ce-details-section padding-around show-it']//div[@class='inline']//div//table[@id='pr']/tbody/tr[" + stri + "]/td[7]", "xpath")
            if strEcoMcoStatus != '':
                objActions.clickElement( "//div[@class='context-ce-details-section padding-around show-it']//div[@class='inline']//div//table[@id='pr']/tbody/tr[" + stri + "]/td[1]", "xpath")
                time.sleep(2)
                MyConfigFiles.driver.find_element_by_name("mcoEco").clear()
                objActions.enterText(PCN.AddNewRecord_ECOMCO_WebEdit_name, "name", "Invailddata")
                objCommon.capture_screenshot("MCOECO Values is edited Sucessfully with invalid data")
                objActions.clickElement(PCN.AddNewAttachement_SubmitBtn_xpath, "xpath")
                time.sleep(1)
                objActions.selectDropdown(PCN.Validate_PCNStatus_Value_name, "name", "visibletext", PCNStatus)
                time.sleep(2)
                objActions.enterText(PCN.Validate_PCNStatusComment_Value_name, "name", pcnComments)
                time.sleep(2)
                objActions.enterText(PCN.PCNStatusClose_Comments_name, "name", pcnClosedComments)
                time.sleep(2)
                objActions.clickElement(PCN.Close_Assessment_WebElement_xpath, "xpath")
                Waring_Msg=objActions.getText(PCN.Close_Assessment_Warning_WebElement_xpath, "xpath")
                print(Waring_Msg)
                assert (objActions.AssertObjectExists(PCN.Close_Assessment_Warning_WebElement_xpath, "xpath"))
                objActions.clickElement(PCN.Completed_Page_OK_button_xpath, "xpath")
                time.sleep(2)
                objActions.clickElement("//div[@class='context-ce-details-section padding-around show-it']//div[@class='inline']//div//table[@id='pr']/tbody/tr[" + stri + "]/td[1]", "xpath")
                time.sleep(2)
                MyConfigFiles.driver.find_element_by_name("mcoEco").clear()
                objActions.clickElement(PCN.AddNewAttachement_SubmitBtn_xpath, "xpath")
                time.sleep(2)
                objActions.clickElement(PCN.Close_Assessment_WebElement_xpath, "xpath")
            break














