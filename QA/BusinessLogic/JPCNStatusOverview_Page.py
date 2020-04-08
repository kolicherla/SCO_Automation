from QA.PageObjects.Test_Locators import PCN
from QA.Utilities.PerformAction import PerformActions
from QA.Utilities.CommonLib import CommonFunctions
from QA.Base.Config import MyConfigFiles
from QA.BusinessLogic.Home_Page import Home
from QA.BusinessLogic.Filter_Page import Filter
from selenium.webdriver.common.keys import Keys
from QA.BusinessLogic.CreateJPCN_Page import createJPCN_Page
from QA.BusinessLogic.SwitchToOtherRoles_Page import SwitchToRoles_Page
from selenium.webdriver.support.ui import Select
from pathlib import Path
import sys

import time

class JPCNstatusoverview_Page():
    global objCommon, objActions ,objConfig,objFilter,objHome,objCreateJPCN,objSwitchToRoles
    objCommon = CommonFunctions()
    objActions = PerformActions()
    objConfig=MyConfigFiles()
    objFilter=Filter()
    objHome=Home()
    objCreateJPCN = createJPCN_Page()
    objSwitchToRoles = SwitchToRoles_Page()


    def ClickContextCE_Create_Items(self):
        time.sleep(2)
        objActions.clickElement(PCN.DashBoard_CreateItem_WebElement_xpath, "xpath")
        objCommon.capture_screenshot('Clicked on Create Item Sections')

    def ClickContextCE_InitialAssessment_Items(self):
        time.sleep(2)
        objActions.clickElement(PCN.DashBoard_InitialAssessment_WebElement_xpath, "xpath")
        objCommon.capture_screenshot('Clicked on InitialAssessment Sections')

    def ClickGCMAssessment_Items(self):
        time.sleep(2)
        objActions.clickElement(PCN.DashBoard_InitialAssessment_WebElement_xpath, "xpath")
        objCommon.capture_screenshot('Clicked on InitialAssessment Sections')

    def ClickDashboard_Link(self):
        time.sleep(3)
        html = MyConfigFiles.driver.find_element_by_tag_name('html')
        html.send_keys(Keys.PAGE_UP)
        time.sleep(2)
        objActions.clickElement(PCN.DashBoard_Button_xpath, "xpath")
        assert (objActions.AssertObjectExists(PCN.DashBoard_Button_xpath, "xpath"))
        print("Dashboard link clicked sucessfully")

    def ClickCoreCE_AssesmnetPending_Items(self):
        time.sleep(2)
        objActions.clickElement(PCN.DashBoard_CoreCEAssessment_WebElement_xpath, "xpath")
        objCommon.capture_screenshot('Clicked on CoreCE Assessment Item Sections')
        time.sleep(3)


    def SelectJCPN(self,JCPNInput):
        global flag
        # self.ClickContextCE_Create_Items()
        time.sleep(3)
        Arrow_existing=objActions.ObjectExists(PCN.JPCNOverview_Table_Arrow_WebElement_xpath, "xpath")
        if Arrow_existing == True:
            objActions.clickElement(PCN.JPCNOverview_Table_Arrow_WebElement_xpath, "xpath")
        if Arrow_existing != True:
            flag=False
        time.sleep(4)
        objTable=MyConfigFiles.driver.find_elements_by_xpath("//table[@id='created-jpcn']/tbody/tr")
        intRowCount=len(objTable)
        time.sleep(3)
        for i in range(2,intRowCount+1):
            stri=str(i)
            strJCPN=objActions.getText("//table[@id='created-jpcn']/tbody/tr["+stri+"]/td[2]","xpath")
            # print(strJCPN)
            if strJCPN==JCPNInput:
                time.sleep(3)
                objActions.clickElement("//table[@id='created-jpcn']/tbody/tr["+stri+"]/td[2]","xpath")
                flag=True
                time.sleep(3)
                # print("JPCN is displayed on Page: "+str(pages))
                break
            time.sleep(2)
        if flag==False:
            sys.exit("FAILED:: Could not find the JPCNNumber: "+JCPNInput)

    # def SelectJCPN(self,JCPNInput):
    #     global flag
    #     time.sleep(2)
    #     # self.ClickContextCE_Create_Items()
    #     strPages=objActions.getText(PCN.ContextCE_TablePage_Count_xpath,"xpath")
    #     strPagesCount=strPages.split(" ")
    #     intPagesCount=int(strPagesCount[4])
    #     if intPagesCount <= 1:
    #         time.sleep(30)
    #     # print("Number of pages displayed: "+str(intPagesCount))
    #     flag=False
    #     for pages in range(1,intPagesCount+1):
    #         objTable=MyConfigFiles.driver.find_elements_by_xpath("//table[@id='created-jpcn']/tbody/tr")
    #         intRowCount=len(objTable)
    #         # print("Rows Count in page "+str(pages)+" is: "+str(intRowCount-1))
    #         for i in range(2,intRowCount+1):
    #             stri=str(i)
    #             strJCPN=objActions.getText("//table[@id='created-jpcn']/tbody/tr["+stri+"]/td[2]","xpath")
    #             # print(strJCPN)
    #             if strJCPN==JCPNInput:
    #                 time.sleep(2)
    #                 objActions.clickElement("//table[@id='created-jpcn']/tbody/tr["+stri+"]/td[2]","xpath")
    #                 flag=True
    #                 # print("JPCN is displayed on Page: "+str(pages))
    #                 break
    #                 time.sleep(10)
    #         if flag==True:
    #             break
    #         else:
    #             time.sleep(3)
    #             objActions.clickElement("//a[text()='"+str(pages+1)+"']","xpath")
    #             time.sleep(4)
    #     if flag==False:
    #         sys.exit("FAILED:: Could not find the JPCNNumber: "+JCPNInput)

    def SendBack_with_AssignBacktoContextCE(self,AssginbackComments):
        time.sleep(4)
        objActions.clickElement(PCN.JPCNStatus_Overivew_Button_xpath, "xpath")
        time.sleep(3)
        objActions.enterText(PCN.AssignBack_Comments_WebEdit_xpath, "xpath", AssginbackComments)
        time.sleep(2)
        assert (objActions.AssertObjectExists(PCN.submit_button_xpath, "xpath"))
        objActions.clickElement(PCN.submit_button_xpath, "xpath")
        objCommon.capture_screenshot("Sendback to Context CE")

    def Reassign_Assessment(self):
        time.sleep(2)
        objActions.clickElement(PCN.DashBoard_ReassignAssessment_WebElement_xpath, "xpath")

    def Validation_OnCoreCE_ManadtoryFields(self,strFilePath,QRAS,QRRC,CoreCERecommendations,CoreCeREComments,ReasonforNC):
        time.sleep(2)
        # objCommon.AttachFile(strFilePath, PCN.QualDataReview_CoreCE_Attachement_xpath, "xpath")
        # time.sleep(3)
        # objActions.clickElement(PCN.QualDateReview_CoreCe_Upload_xpath, "xpath")
        # time.sleep(4)
        time.sleep(2)
        objActions.selectDropdown(PCN.QualReport_AcceptStaus_CoreCE_xpath, "xpath", "visibletext", QRAS)
        time.sleep(3)
        objActions.enterText(PCN.QualReport_ReviewComments_CoreCE_xpath, "xpath", QRRC)
        time.sleep(2)
        objActions.selectDropdown(PCN.CoreCe_Recommendation_name, "name", "visibletext", CoreCERecommendations)
        time.sleep(2)
        objActions.enterText(PCN.CoreCe_Recommendation_comments_name, "name", CoreCeREComments)
        time.sleep(3)
        self.CoreCE_PCN_ChangeComplianceSelect_Validations(ReasonforNC)
        time.sleep(2)
        strMsg1=objActions.getText(PCN.CoreCE_ChangeStatus_xapth, "xpath")
        strMsg2=objActions.getText(PCN.CoreCE_Gobackmsg_xpath, "xpath")
        strValidationMsg= strMsg1 + strMsg2
        time.sleep(2)
        print("Display Validations message" +strValidationMsg)
        time.sleep(2)


    def Goabck_button(self):
        time.sleep(3)
        objActions.clickElement(PCN.Goback_Button_xpath, "xpath")
        time.sleep(3)
        # self.CoreCE_PCN_ChangeComplianceSelect_Validations(ReasonforNC)

    def Submit_CoreCE_Assessment(self):
        objActions.clickElement(PCN.submit_button_xpath, "xpath")
        time.sleep(3)
        objActions.clickElement(PCN.DashBoard_CoreCECompAssessment_WebElement_xpath, "xpath")
        time.sleep(3)
        self.SelectJCPN()
        time.sleep(3)
        JPCNStatus=objActions.getText(PCN.JPCN_Analyis_Stage_Status_xpath, "xpath")
        print("JPCN Analyis stage is completed sucessfully" +JPCNStatus)
        objCommon.capture_screenshot("JPCN Closed sucessfully")



    def CoreCE_PCN_ChangeComplianceSelect_Validations(self,ReasonforNC):
        time.sleep(3)
        # strPCNComplience = objActions.getText(PCN.PCNCompliance_CoreCE_SelectBox_xpath, "xpath")
        strPCNComplience = objActions.ValidationOnSelectedtext(PCN.Compliance_CoreCE_SelectBox_xpath, "xpath")
        print(strPCNComplience)
        time.sleep(2)
        if strPCNComplience == "Compliant":
            time.sleep(2)
            objActions.selectDropdown(PCN.Compliance_CoreCE_SelectBox_xpath, "xpath", "visibletext", "Non-Compliant")
            time.sleep(2)
            objActions.selectDropdown(PCN.PCNReason_NonCompliance_CoreCE_SelectBox_xpath, "xpath", "visibletext", ReasonforNC)
            time.sleep(2)
            CoreCEJustification= objCreateJPCN.GenerateRandominteger()
            objActions.enterText(PCN.CoreCE_Justifications_name, "name", CoreCEJustification)

        else:
            time.sleep(2)
            objActions.selectDropdown(PCN.Compliance_CoreCE_SelectBox_xpath, "xpath", "visibletext", "Compliant")
            time.sleep(2)
            objActions.enterText(PCN.CoreCE_Justifications_name, "name", "Justificaion")
            time.sleep(3)
        objActions.clickElement(PCN.Complete_Assessment_Button_xpath, "xpath")


    def Verify_Save_For_Commodity_Manager(self,strJPNID):
        time.sleep(2)
        objActions.clickElement(PCN.DashBoard_GCMAssessment_WebElement_xpath, "xpath")
        objCommon.capture_screenshot("GCM Assessment JPCN Status Overview")
        time.sleep(2)
        self.SelectJCPN(strJPNID)
        time.sleep(2)
        SignoffComments= objCreateJPCN.GenerateRandominteger()
        objActions.enterText(PCN.GCM_Signoff_Comments_WebEdit_name, "name", SignoffComments)
        objActions.clickElement(PCN.GCM_Save_Button_xpath, "xpath")
        time.sleep(2)
        objActions.clickElement(PCN.DashBoard_GCMAssessment_WebElement_xpath, "xpath")
        self.SelectJCPN(strJPNID)
        time.sleep(2)
        return SignoffComments

    def Verify_Close_For_Commodity_Manager(self,strJPNID):
        time.sleep(2)
        objActions.clickElement(PCN.GCM_Close_Button_xpath, "xpath")
        strCIP_Msg=objActions.getText(PCN.GCM_CIPUncheck_Msg_text_xapth, "xpath")
        if strCIP_Msg=="Please check Inventory Position before closing the PCN/PDN":
            print("Checked Inventory Position check box is Manadatory to close GCM Assessemnt")
            objCommon.capture_screenshot("Checked Inventory Position is Manadatory Check box ")
            time.sleep(2)
            objActions.clickElement(PCN.GCM_CIP_WebElement_name, "name")
            objActions.clickElement(PCN.GCM_Close_Button_xpath, "xpath")
            time.sleep(2)
            objSwitchToRoles.SwitchToRole("Core CE")
            self.ClickDashboard_Link()
            objActions.clickElement(PCN.DashBoard_CoreCEAssessment_WebElement_xpath, "xpath")
            time.sleep(3)
            self.SelectJCPN(strJPNID)



    def Verify_GCMTable_SignoffComments(self):
        global flag
        time.sleep(2)
        flag=False
        objTable=MyConfigFiles.driver.find_elements_by_xpath("//table[@id='gcm-tab']/tbody/tr")
        intRowCount=len(objTable)
        for i in range(2,intRowCount+1):
            stri=str(i)
            strSignoff_Comments=objActions.getText("//table[@id='gcm-tab']/tbody/tr["+stri+"]/td[5]","xpath")
            time.sleep(2)
            strClosure_Comments=objActions.getAttributeValue(PCN.GCM_Signoff_Comments_WebEdit_name, "name", "value")
            # print(strJCPN)
            if strSignoff_Comments==strClosure_Comments:
                time.sleep(2)
                print("comments Sucessfully displayed in:"+strClosure_Comments+ " " "signoffSection:" +strSignoff_Comments)
                flag=True
                break
            time.sleep(3)
        if flag==False:
            sys.exit("FAILED:: Could not find the Closure_Comments:")


    def Compare_GCM_JPCN(self,JCPNInput):
        global flag
        time.sleep(2)
        # self.ClickContextCE_Create_Items()
        strPages=objActions.getText(PCN.ContextCE_TablePage_Count_xpath,"xpath")
        strPagesCount=strPages.split(" ")
        intPagesCount=int(strPagesCount[4])
        if intPagesCount <= 1:
            time.sleep(30)
            flag=False
            for pages in range(1,intPagesCount+1):
                objTable=MyConfigFiles.driver.find_elements_by_xpath("//table[@id='created-jpcn']/tbody/tr")
                intRowCount=len(objTable)
                # print("Rows Count in page "+str(pages)+" is: "+str(intRowCount-1))
                for i in range(2,intRowCount+1):
                    stri=str(i)
                    strJCPN=objActions.getText("//table[@id='created-jpcn']/tbody/tr["+stri+"]/td[2]","xpath")
                    # print(strJCPN)
                    if strJCPN!=JCPNInput:
                        time.sleep(2)
                        flag=True
                        # print("JPCN is displayed on Page: "+str(pages))
                if flag==True:
                    break
                else:
                    time.sleep(3)
                    objActions.clickElement("//a[text()='"+str(pages+1)+"']","xpath")
                    time.sleep(4)
            if flag==False:
                sys.exit("FAILED:: Could not find the JPCNNumber: "+JCPNInput)




















