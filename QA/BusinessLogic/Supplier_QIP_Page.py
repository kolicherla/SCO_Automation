from QA.PageObjects.Test_Locators import QET
from QA.Utilities.PerformAction import PerformActions
from QA.Utilities.CommonLib import CommonFunctions
from QA.Base.Config import MyConfigFiles
from QA.BusinessLogic.Home_Page import Home
from QA.BusinessLogic.Filter_Page import Filter
import time

class SupplierQIP():
    global objCommon, objActions, objConfig,objHome,objFilter
    objCommon = CommonFunctions()
    objActions = PerformActions()
    objConfig=MyConfigFiles()
    objFilter=Filter()
    objHome=Home()

    # Adding Containment to the QIP by loggin in with Supplier login Credentials
    def Supplier_AddingContainment(self, QIPID, CA_Title, CA_Description, Supplier_QIPteam):
        objFilter.NavigateToQIP(QIPID)
        objActions.clickElement(QET.AddCA_button_xpath, "xpath")
        self.AddAction(CA_Title, CA_Description)
        objActions.clickElement(QET.MarkAsCompleted_button_xpath, "xpath")
        objCommon.capture_screenshot("Marked as completed")
        objActions.clickElement(QET.Confirm_button_xpath, "xpath")
        assert (objActions.AssertObjectExists(QET.QIPIssued_WebElement_xpath, "xpath"))
        objCommon.capture_screenshot("QIP Issued to Supplier")
        time.sleep(2)
        objActions.selectDropdown(QET.Supplierlogin_QIPteam_Selectbox_xpath, "xpath", "visibletext", Supplier_QIPteam)
        objActions.clickElement(QET.Supplier_QIPteam_Update_btn_xpath, "xpath")
        # objActions.clickElement(QET.ECDForRCCA_WebEdit_xpath, "xpath")
        # self.selectCurrentDay()
        objActions.clickElement(QET.Supplier_SubmittedContainmentPlan_button_xpath, "xpath")
        assert (objActions.AssertObjectExists(QET.SubmittedContainmentplan_WebElement_xpath, "xpath"))
        CSubmitPlan_ACD= objActions.getText(QET.ACDDate_WebElement_xpath, "xpath")
        print("ACD date after submited the Containment paln:" +CSubmitPlan_ACD )
        objCommon.capture_screenshot("Supplier Containment plan submitted")

    # method the select curret day in the Action
    def selectCurrentDay(self):
        intDay = str(objCommon.GetCurrentDay()).replace("0", '')
        # Concenate it with "day-" to satisfy the xpath
        strConcDate = "day-" + str(intDay)
        objActions.clickElement("//div[not(contains(@class,'disabled'))][@aria-label='" + strConcDate + "']", "xpath")

    def Supplier_Containment_DeleteAction(self, QIPID, CA_Title, CA_Description):
        objFilter.NavigateToQIP(QIPID)
        objActions.clickElement(QET.AddCA_button_xpath, "xpath")
        self.AddAction(CA_Title, CA_Description)
        objActions.clickElement(QET.DeleteAction_button_xpath, "xpath")
        objActions.clickElement(QET.Confirm_button_xpath, "xpath")
        objCommon.capture_screenshot("Deleted Containment Action")
        # objActions.AssertObjectExists(QET.AddCA_button_xpath,"xpath")
        assert (objActions.AssertObjectExists(QET.AddCA_button_xpath, "xpath"))

        # Adding Action(can be used for any of the flows
    def AddAction(self, CA_Title, CA_Description):
        objActions.clickElement(QET.CA_Title_WebEdit_xpath, "xpath")
        objActions.enterText(QET.CA_Title_WebEdit_xpath, "xpath", CA_Title)
        objActions.enterText(QET.CA_Description_WebEdit_xpath, "xpath", CA_Description)
        time.sleep(2)
        objActions.clickElement(QET.ECD_WebEdit_xpath, "xpath")
        self.selectCurrentDay()
        time.sleep(1)
        objActions.clickElement(QET.Save_button_xpath, "xpath")

        # Method to check if the action is editable
    def EditAction(self, CA_UpdatedTitle):
        time.sleep(1)
        strCA_Title = objActions.getText(QET.ActionTitle_WebElement_xpath, "xpath")
        print("Title before update:" + strCA_Title)
        objActions.clickElement(QET.EditAction_button_xpath, "xpath")
        objActions.enterText(QET.CA_Title_WebEdit_xpath, "xpath", CA_UpdatedTitle)
        objActions.clickElement(QET.Save_button_xpath, "xpath")
        time.sleep(1)
        strUpdatedTitle = objActions.getText(QET.ActionTitle_WebElement_xpath, "xpath")
        print("Title After update should be:" + strUpdatedTitle)
        if strCA_Title != strUpdatedTitle:
            print("Successfully Edited Containment to-" + strUpdatedTitle)
        else:
            print("Could not Edit Containment to-" + strUpdatedTitle)
            assert strCA_Title != strUpdatedTitle

    def Supplier_EditContainment(self, QIPID, CA_Title, CA_Description, CA_UpdatedTitle):
        objFilter.NavigateToQIP(QIPID)
        objActions.clickElement(QET.AddCA_button_xpath, "xpath")
        self.AddAction(CA_Title, CA_Description)
        self.EditAction(CA_UpdatedTitle)
        objCommon.capture_screenshot("Edited Action")


    def Supplier_EditRCCA(self,QIPID,CA_Title,CA_Description,CA_UpdatedTitle):
        objFilter.NavigateToQIP(QIPID)
        #Root Cause Analysis
        objActions.clickElement(QET.AddRCAction_button_xpath, "xpath")
        self.AddAction(CA_Title, CA_Description)
        self.EditAction(CA_UpdatedTitle)
        objCommon.capture_screenshot("Edited Action")

    def Supplier_RCCA_DeleteAction(self,QIPID,CA_Title,CA_Description):
        objFilter.NavigateToQIP(QIPID)
        objActions.clickElement(QET.AddRCAction_button_xpath, "xpath")
        self.AddAction(CA_Title, CA_Description)
        objActions.clickElement(QET.DeleteAction_button_xpath,"xpath")
        objActions.clickElement(QET.Confirm_button_xpath,"xpath")
        objCommon.capture_screenshot("Deleted RCCA Action")
        assert (objActions.AssertObjectExists(QET.AddRCAction_button_xpath,"xpath"))

    def Supplier_AddRCCA(self,QIPID,CA_Title,CA_Description):
        objFilter.NavigateToQIP(QIPID)
        #Root Cause Analysis
        objActions.clickElement(QET.AddRCAction_button_xpath, "xpath")
        self.AddAction(CA_Title,CA_Description)
        objActions.clickElement(QET.MarkAsCompleted_button_xpath, "xpath")
        objCommon.capture_screenshot("Adding Root Cause Analysis")
        objActions.clickElement(QET.Confirm_button_xpath, "xpath")

        #Corrective Actions
        time.sleep(2)
        objActions.clickElement(QET.AddCorrectiveActions_button_xpath, "xpath")
        self.AddAction(CA_Title,CA_Description)
        objActions.clickElement(QET.MarkAsCompleted_button_xpath, "xpath")
        objCommon.capture_screenshot("Adding Corrective Actions")
        objActions.clickElement(QET.Confirm_button_xpath, "xpath")
        # Preventive Actions
        time.sleep(2)
        objActions.clickElement(QET.AddPAAction_button_xpath, "xpath")
        self.AddAction(CA_Title, CA_Description)
        objActions.clickElement(QET.MarkAsCompleted_button_xpath, "xpath")
        objCommon.capture_screenshot("Adding Preventive Actions")
        objActions.clickElement(QET.Confirm_button_xpath, "xpath")
        time.sleep(3)
        objActions.clickElement(QET.SubmitRCCAPlan_Button_xpath,"xpath")
        objCommon.capture_screenshot("Supplier submitted RCCA Plan")
        RCCA_Plan_ECD= objActions.getText(QET.ECDDate_WebElement_xpath, "xpath")
        print(" RCCA Paln ECD date" +RCCA_Plan_ECD)
        assert(objActions.AssertObjectExists(QET.Supplier_RCCAPlansubmitted_WebElement_xapth,"xpath"))


    def Supplier_ECDForRCCA_AddingContainment(self, QIPID, CA_Title, CA_Description, ECDDays):
        objFilter.NavigateToQIP(QIPID)
        # objActions.clickElement(QET.ECDForRCCA_WebEdit_xpath, "xpath")
        # time.sleep(1)
        # objActions.clickElement(QET.ECDNextDay_button_xpath, "xpath")
        # objActions.clickElement(QET.ECDNextDay_button_xpath, "xpath")
        # intDay = objCommon.ModifyDay("add", ECDDays)
        # # Concenate it with "day-" to satisfy the xpath
        # strConcDate = "day-" + str(intDay)
        # objActions.clickElement("//div[not(contains(@class,'disabled'))][@aria-label='" + strConcDate + "']",
        #                         "xpath")
        # time.sleep(1)
        objActions.clickElement(QET.AddCA_button_xpath, "xpath")
        self.AddAction(CA_Title, CA_Description)
        objActions.clickElement(QET.MarkAsCompleted_button_xpath, "xpath")
        objActions.clickElement(QET.Confirm_button_xpath, "xpath")
        objActions.clickElement(QET.SubmitForApproval_Button_xpath, "xpath")
        objCommon.capture_screenshot("Submit For Approval with RCCA Due Date")

    def Supplier_AddRCCAWithoutSubmit(self,QIPID,CA_Title,CA_Description):
        objFilter.NavigateToQIP(QIPID)
        # Root Cause Analysis
        objActions.clickElement(QET.AddRCAction_button_xpath, "xpath")
        self.AddAction(CA_Title, CA_Description)
        objActions.clickElement(QET.MarkAsCompleted_button_xpath, "xpath")
        objCommon.capture_screenshot("Adding Root Cause Analysis")
        objActions.clickElement(QET.Confirm_button_xpath, "xpath")

        # Corrective Actions
        time.sleep(2)
        objActions.clickElement(QET.AddCorrectiveActions_button_xpath, "xpath")
        self.AddAction(CA_Title, CA_Description)
        objActions.clickElement(QET.MarkAsCompleted_button_xpath, "xpath")
        objCommon.capture_screenshot("Adding Corrective Actions")
        objActions.clickElement(QET.Confirm_button_xpath, "xpath")

        # Preventive Actions
        time.sleep(2)
        objActions.clickElement(QET.AddPAAction_button_xpath, "xpath")
        self.AddAction(CA_Title, CA_Description)
        objActions.clickElement(QET.MarkAsCompleted_button_xpath, "xpath")
        objCommon.capture_screenshot("Adding Corrective Actions")
        objActions.clickElement(QET.Confirm_button_xpath, "xpath")

    def SupplierRequestExtension(self,QIPID,ExtensionDays,ExtensionReason):
        time.sleep(2)
        objFilter.NavigateToQIP(QIPID)
        strECDDate=self.ECDDate()
        # print("ECD date before request for extension is :"+strECDDate)
        time.sleep(2)
        objActions.clickElement(QET.RequestExtesnion_button_xpath,"xpath")
        objActions.clickElement(QET.ExtendTo_WebEdit_xpath,"xpath")
        time.sleep(2)
        self.selectFutureDay(ExtensionDays)
        objActions.enterText(QET.ReasonForExtension_WebEdit_xpath,"xpath",ExtensionReason)
        objActions.clickElement(QET.Confirm_button_xpath,"xpath")
        objCommon.capture_screenshot("Reason for extension applied")
        time.sleep(2)
        assert (objActions.AssertObjectExists(QET.Supplier_RCCAECDAuto_extended_WebElement_xapth, "xpath"))
        strUpdatedECDDate = self.ECDDate()
        # print("Updated ECD date after request for extension is:"+strUpdatedECDDate)
        strModifiedDate=objCommon.ModifyDateFrom(strECDDate,"add",ExtensionDays)
        # print("ECD date to be dispalyed is:"+strModifiedDate)
        if strUpdatedECDDate==strModifiedDate:
            print("ECD date is auto set to days: "+ str(ExtensionDays))
        else:
            print("ECD date is not auto set to days"+ str(ExtensionDays))
        assert strUpdatedECDDate==strModifiedDate
        objActions.clickElement(QET.SubmitForApproval_Button_xpath,"xpath")
        time.sleep(2)
        objCommon.capture_screenshot("Request for extension successfull")
        assert (objActions.AssertObjectExists(QET.Supplier_CRCCAAction_Sub_WebElement_xpath, "xpath"))

    def ECDDate(self):
        strECDText = objActions.getText(QET.ECDDate_WebElement_xpath, "xpath")
        return strECDText.split(":")[1]

    def selectFutureDay(self,ExtensionDays):
        intDay = str(objCommon.ModifyDay("add", ExtensionDays)).replace("0",'')
        strConcDate = "day-" + str(intDay)
        time.sleep(2)
        try:
            objConfig.driver.find_element_by_xpath("//div[not(contains(@class,'disabled'))][@aria-label='" + strConcDate + "']").click()
        except:
            print("Moved to next month")
            objActions.clickElement(QET.ECDNextDay_button_xpath,"xpath")
            objConfig.driver.find_element_by_xpath(
                "//div[not(contains(@class,'disabled'))][@aria-label='" + strConcDate + "']").click()

    def Supplier_EditDeliverables(self,QIPID,CA_Title,CA_Description,CA_UpdatedTitle):
        objFilter.NavigateToQIP(QIPID)
        time.sleep(2)
        objActions.clickElement(QET.AddDeliverables_button_xpath, "xpath")
        self.AddAction(CA_Title,CA_Description)
        self.EditAction(CA_UpdatedTitle)
        objCommon.capture_screenshot("Edited Action")

    def Supplier_AddDeliverables(self, QIPID, CA_Title, CA_Description):
        objFilter.NavigateToQIP(QIPID)
        objActions.clickElement(QET.AddDeliverables_button_xpath, "xpath")
        self.AddAction(CA_Title, CA_Description)
        objActions.clickElement(QET.MarkAsCompleted_button_xpath, "xpath")
        objCommon.capture_screenshot("Adding Deliverables")
        objActions.clickElement(QET.Confirm_button_xpath, "xpath")
        time.sleep(2)
        objActions.clickElement(QET.QIP_Accept_button_xpath, "xpath")
        objCommon.capture_screenshot("Juniper Completed and Approved QIP validation")
        assert (objActions.AssertObjectExists(QET.jrCompletedandApprove_validation_WebElemnt_xpath, "xpath"))

    def Supplier_Validation_DeleteAction(self,QIPID,CA_Title,CA_Description):
        objFilter.NavigateToQIP(QIPID)
        objActions.clickElement(QET.AddDeliverables_button_xpath, "xpath")
        self.AddAction(CA_Title, CA_Description)
        objActions.clickElement(QET.DeleteAction_button_xpath,"xpath")
        objActions.clickElement(QET.Confirm_button_xpath,"xpath")
        objCommon.capture_screenshot("Deleted RCCA Action")
        # objActions.AssertObjectExists(QET.AddCA_button_xpath,"xpath")
        assert (objActions.AssertObjectExists(QET.AddDeliverables_button_xpath,"xpath"))

    def Supplier_AddDeliverables_RequestExtension(self,QIPID,CA_Title,CA_Description):
        objFilter.NavigateToQIP(QIPID)
        objActions.clickElement(QET.AddDeliverables_button_xpath, "xpath")
        self.AddAction(CA_Title,CA_Description)
        objActions.clickElement(QET.MarkAsCompleted_button_xpath, "xpath")
        objCommon.capture_screenshot("Adding Deliverables")
        objActions.clickElement(QET.Confirm_button_xpath, "xpath")

    def User_Extend_Validation(self,QIPID,ExtensionDays,ExtensionReason):
        time.sleep(2)
        objFilter.NavigateToQIP(QIPID)
        strECDDate=self.ECDDate()
        print("ECD date before request for extension is :"+strECDDate)
        time.sleep(2)
        objActions.clickElement(QET.QIP_Extend_validation_button_xpath,"xpath")
        objActions.clickElement(QET.ExtendTo_WebEdit_xpath,"xpath")
        time.sleep(2)
        self.selectFutureDay(ExtensionDays)
        objActions.enterText(QET.ReasonForExtension_WebEdit_xpath,"xpath",ExtensionReason)
        objActions.clickElement(QET.Confirm_button_xpath,"xpath")
        objCommon.capture_screenshot("Reason for extension applied")
        time.sleep(2)
        assert (objActions.AssertObjectExists(QET.jn_ValidationETC_Extend_WebElement_xapth, "xpath"))
        strUpdatedECDDate = self.ECDDate()
        print("Updated ECD date after request for extension is:"+strUpdatedECDDate)
        strModifiedDate=objCommon.ModifyDateFrom(strECDDate,"add",ExtensionDays)
        print("ECD date to be dispalyed is:"+strModifiedDate)
        if strUpdatedECDDate==strModifiedDate:
            print("ECD date is auto set to days: "+ str(ExtensionDays))
        else:
            print("ECD date is not auto set to days"+ str(ExtensionDays))
        assert strUpdatedECDDate==strModifiedDate
        objCommon.capture_screenshot("Request for extension successfull")



