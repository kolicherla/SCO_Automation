from QA.PageObjects.Test_Locators import QET
from QA.Utilities.PerformAction import PerformActions
from QA.Utilities.CommonLib import CommonFunctions
from QA.Base.Config import MyConfigFiles
from QA.BusinessLogic.Home_Page import Home
from QA.BusinessLogic.Filter_Page import Filter
import time

class SupplierSCAR():
    global objCommon, objActions, objConfig,objHome,objFilter
    objCommon = CommonFunctions()
    objActions = PerformActions()
    objConfig=MyConfigFiles()
    objFilter=Filter()
    objHome=Home()

    # Adding Containment to the SCAR by loggin in with Supplier login Credentials
    def Supplier_AddingContainment(self, ScarID, CA_Title, CA_Description):
        objFilter.NavigateToSCAR(ScarID)
        objActions.clickElement(QET.AddCA_button_xpath, "xpath")
        self.AddAction(CA_Title, CA_Description)
        objActions.clickElement(QET.MarkAsCompleted_button_xpath, "xpath")
        objCommon.capture_screenshot("Marked as completed")
        objActions.clickElement(QET.Confirm_button_xpath, "xpath")
        assert (objActions.AssertObjectExists(QET.ScarIssued_WebElement_xpath, "xpath"))
        objCommon.capture_screenshot("SCAR Issued")
        time.sleep(2)
        objActions.clickElement(QET.ECDForRCCA_WebEdit_xpath, "xpath")
        self.selectCurrentDay()
        objActions.clickElement(QET.SubmitForApproval_Button_xpath, "xpath")
        assert (objActions.AssertObjectExists(QET.SubmittedContainment_WebElement_xpath, "xpath"))
        objCommon.capture_screenshot("Supplier submitted Containment actions and RCCA due date")

    # method the select curret day in the Action
    def selectCurrentDay(self):
        intDay = str(objCommon.GetCurrentDay()).replace("0", '')
        # Concenate it with "day-" to satisfy the xpath
        strConcDate = "day-" + str(intDay)
        objActions.clickElement("//div[not(contains(@class,'disabled'))][@aria-label='" + strConcDate + "']",
                                "xpath")

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



    def Supplier_ECDForRCCA_AddingContainment(self, ScarID, CA_Title, CA_Description, ECDDays):
        objFilter.NavigateToSCAR(ScarID)
        objActions.clickElement(QET.ECDForRCCA_WebEdit_xpath, "xpath")
        time.sleep(1)
        objActions.clickElement(QET.ECDNextDay_button_xpath, "xpath")
        objActions.clickElement(QET.ECDNextDay_button_xpath, "xpath")
        intDay = objCommon.ModifyDay("add", ECDDays)
        # Concenate it with "day-" to satisfy the xpath
        strConcDate = "day-" + str(intDay)
        objActions.clickElement("//div[not(contains(@class,'disabled'))][@aria-label='" + strConcDate + "']",
                                "xpath")
        time.sleep(1)
        objActions.clickElement(QET.AddCA_button_xpath, "xpath")
        self.AddAction(CA_Title, CA_Description)
        objActions.clickElement(QET.MarkAsCompleted_button_xpath, "xpath")
        objActions.clickElement(QET.Confirm_button_xpath, "xpath")
        objActions.clickElement(QET.SubmitForApproval_Button_xpath, "xpath")
        objCommon.capture_screenshot("Submit For Approval with RCCA Due Date")

    def Supplier_EditContainment(self, ScarID, CA_Title, CA_Description, CA_UpdatedTitle):
        objFilter.NavigateToSCAR(ScarID)
        objActions.clickElement(QET.AddCA_button_xpath, "xpath")
        self.AddAction(CA_Title, CA_Description)
        self.EditAction(CA_UpdatedTitle)
        objCommon.capture_screenshot("Edited Action")

    def Supplier_Containment_DeleteAction(self, ScarID, CA_Title, CA_Description):
        objFilter.NavigateToSCAR(ScarID)
        objActions.clickElement(QET.AddCA_button_xpath, "xpath")
        self.AddAction(CA_Title, CA_Description)
        objActions.clickElement(QET.DeleteAction_button_xpath, "xpath")
        objActions.clickElement(QET.Confirm_button_xpath, "xpath")
        objCommon.capture_screenshot("Deleted Containment Action")
        # objActions.AssertObjectExists(QET.AddCA_button_xpath,"xpath")
        assert (objActions.AssertObjectExists(QET.AddCA_button_xpath, "xpath"))

    def Supplier_AddRCCA(self,ScarID,CA_Title,CA_Description):
        objFilter.NavigateToSCAR(ScarID)
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
        time.sleep(2)
        objActions.clickElement(QET.SubmitForApproval_Button_xpath,"xpath")
        objCommon.capture_screenshot("Supplier submitted RCCA for Juniper Approval")
        assert(objActions.AssertObjectExists(QET.SuSubmittedRCCAforJnApproval_WebElement_xpath,"xpath"))


    def Supplier_AddRCCAWithoutSubmit(self,ScarID,CA_Title,CA_Description):
        objFilter.NavigateToSCAR(ScarID)
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
        time.sleep(2)

    def Supplier_AddDeliverables(self,ScarID,CA_Title,CA_Description):
        objFilter.NavigateToSCAR(ScarID)
        objActions.clickElement(QET.AddDeliverables_button_xpath, "xpath")
        self.AddAction(CA_Title,CA_Description)
        objActions.clickElement(QET.MarkAsCompleted_button_xpath, "xpath")
        objCommon.capture_screenshot("Adding Deliverables")
        objActions.clickElement(QET.Confirm_button_xpath, "xpath")
        time.sleep(2)
        objActions.clickElement(QET.SubmitForApproval_Button_xpath, "xpath")
        objCommon.capture_screenshot("Supplier submitted Validation deliverables for Juniper Approval")
        assert(objActions.AssertObjectExists(QET.SubmittedValidationDeliverables_WebElement_xpath, "xpath"))


    def Supplier_AddDeliverables_RequestExtension(self,ScarID,CA_Title,CA_Description):
        objFilter.NavigateToSCAR(ScarID)
        objActions.clickElement(QET.AddDeliverables_button_xpath, "xpath")
        self.AddAction(CA_Title,CA_Description)
        objActions.clickElement(QET.MarkAsCompleted_button_xpath, "xpath")
        objCommon.capture_screenshot("Adding Deliverables")
        objActions.clickElement(QET.Confirm_button_xpath, "xpath")



    def Supplier_EditDeliverables(self,ScarID,CA_Title,CA_Description,CA_UpdatedTitle):
        objFilter.NavigateToSCAR(ScarID)
        objActions.clickElement(QET.AddDeliverables_button_xpath, "xpath")
        self.AddAction(CA_Title,CA_Description)
        self.EditAction(CA_UpdatedTitle)
        objCommon.capture_screenshot("Edited Action")


    def Supplier_Validation_DeleteAction(self,ScarID,CA_Title,CA_Description):
        objFilter.NavigateToSCAR(ScarID)
        objActions.clickElement(QET.AddDeliverables_button_xpath, "xpath")
        self.AddAction(CA_Title, CA_Description)
        objActions.clickElement(QET.DeleteAction_button_xpath,"xpath")
        objActions.clickElement(QET.Confirm_button_xpath,"xpath")
        objCommon.capture_screenshot("Deleted RCCA Action")
        # objActions.AssertObjectExists(QET.AddCA_button_xpath,"xpath")
        assert (objActions.AssertObjectExists(QET.AddDeliverables_button_xpath,"xpath"))


    def Supplier_EditRCCA(self,ScarID,CA_Title,CA_Description,CA_UpdatedTitle):
        objFilter.NavigateToSCAR(ScarID)
        #Root Cause Analysis
        objActions.clickElement(QET.AddRCAction_button_xpath, "xpath")
        self.AddAction(CA_Title, CA_Description)
        self.EditAction(CA_UpdatedTitle)
        objCommon.capture_screenshot("Edited Action")

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


    def Supplier_RCCA_DeleteAction(self,ScarID,CA_Title,CA_Description):
        objFilter.NavigateToSCAR(ScarID)
        objActions.clickElement(QET.AddRCAction_button_xpath, "xpath")
        self.AddAction(CA_Title, CA_Description)
        objActions.clickElement(QET.DeleteAction_button_xpath,"xpath")
        objActions.clickElement(QET.Confirm_button_xpath,"xpath")
        objCommon.capture_screenshot("Deleted RCCA Action")
        assert (objActions.AssertObjectExists(QET.AddRCAction_button_xpath,"xpath"))

    def SupplierRequestExtension(self,ExtensionDays,ExtensionReason):
        strECDDate=self.ECDDate()
        print("ECD date before request for extension is :"+strECDDate)
        time.sleep(2)
        objActions.clickElement(QET.RequestExtesnion_button_xpath,"xpath")
        objActions.clickElement(QET.ExtendTo_WebEdit_xpath,"xpath")
        time.sleep(2)
        self.selectFutureDay(ExtensionDays)
        objActions.enterText(QET.ReasonForExtension_WebEdit_xpath,"xpath",ExtensionReason)
        objActions.clickElement(QET.Confirm_button_xpath,"xpath")
        objCommon.capture_screenshot("Reason for extension applied")
        strUpdatedECDDate = self.ECDDate()
        print("Updated ECD date after request for extension is:"+strUpdatedECDDate)
        strModifiedDate=objCommon.ModifyDateFrom(strECDDate,"add",ExtensionDays)
        print("ECD date to be dispalyed is:"+strModifiedDate)
        if strUpdatedECDDate==strModifiedDate:
            print("ECD date is auto set to days: "+ str(ExtensionDays))
        else:
            print("ECD date is not auto set to days"+ str(ExtensionDays))
        assert strUpdatedECDDate==strModifiedDate
        objActions.clickElement(QET.SubmitForApproval_Button_xpath,"xpath")
        time.sleep(2)
        objCommon.capture_screenshot("Request for extension successfull")


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