from QA.PageObjects.Test_Locators import QET
from QA.Utilities.PerformAction import PerformActions
from QA.Utilities.CommonLib import CommonFunctions
from QA.Base.Config import MyConfigFiles
from QA.BusinessLogic.Home_Page import Home
from QA.BusinessLogic.Filter_Page import Filter
import time

class createSCAR_Page():
    global objCommon, objActions, objConfig,objHome,objFilter
    objCommon = CommonFunctions()
    objActions = PerformActions()
    objConfig=MyConfigFiles()
    objFilter=Filter()
    objHome=Home()


#Method to create the SCAR
    def CreateSCAR(self, ProblemDescription, AffectedPart, UserGroup, Supplier, Contact, Escalation, Jn_Escalation,
                   JnWatchlist):
        objDic = dict();
        objHome.ClickSCARButton()
        time.sleep(2)
        objFilter.ClickCreate()
        objActions.enterText(QET.ProblemDescription_WebEdit_xpath, "xpath", ProblemDescription)
        objActions.clickElement(QET.AffectedPart_webEdit_xpath, "xpath")
        time.sleep(2)
        objActions.clickElement("//li[@data-part='" + AffectedPart + "']", "xpath")
        objActions.selectDropdown(QET.SCAR_UserGroup_SelectBox_xpath, "xpath", "value", UserGroup)
        time.sleep(2)
        objActions.selectDropdown(QET.Supplier_SelectBox_xpath, "xpath", "visibletext", Supplier)
        objActions.selectDropdown(QET.Contact_SelectBox_xpath, "xpath", "visibletext", Contact)
        objActions.selectDropdown(QET.Escalation_SelectBox_xpath, "xpath", "visibletext", Escalation)
        objActions.enterText(QET.Escalation_WebEdit_xpath, "xpath", Jn_Escalation)
        time.sleep(2)
        objActions.clickElement("//span[text()='" + Jn_Escalation + "']", "xpath")
        time.sleep(2)
        objActions.clickElement(QET.SupplierWatchList_WebEdit_xpath, "xpath")
        objActions.clickElement("//option[@data-type='contact' and text()='" + JnWatchlist + "']", "xpath")
        objActions.clickElement(QET.CreateScar_button_xpath, "xpath")
        objCommon.capture_screenshot('SCAR Created Successfully')
        strSCARID = objActions.getText(QET.ScarID_WebElement_xpath, "xpath")
        print("SCAR Created successfully with ID:" + strSCARID)
        strURL = objActions.getURL()
        objDic['URL'] = strURL
        objDic['ScarID'] = strSCARID
        return objDic


#Issuing the SCAR
    def IssueSCAR(self):
        #time.sleep(2)
        objActions.clickElement(QET.IssueScar_button_xpath, "xpath")
        assert(objActions.AssertObjectExists(QET.ScarIssued_WebElement_xpath,"xpath"))
        objCommon.capture_screenshot("SCAR Issued Successfully")



    def User_ApproveSCAR(self,ScarID):
        objFilter.NavigateToSCAR(ScarID)
        objActions.clickElement(QET.Approve_button_xpath, "xpath")
        objActions.clickElement(QET.Confirm_button_xpath, "xpath")
        objCommon.capture_screenshot("SCAR Issued")
        assert(objActions.AssertObjectExists(QET.JnApprovedContainmentActions_webElement_xpath, "xpath"))


    def User_RejectSCAR(self,ScarID,RejectionComments):
        objFilter.NavigateToSCAR(ScarID)
        objActions.clickElement(QET.Reject_button_xpath, "xpath")
        objActions.enterText(QET.RejectionComments_WebEdit_xpath,"xpath",RejectionComments)
        objActions.clickElement(QET.Confirm_button_xpath,"xpath")
        objCommon.capture_screenshot("Containment Actions Rejected")
        assert (objActions.AssertObjectExists(QET.RejectedContainment_WebElement_xpath,"xpath"))


    def User_RejectRCCA(self,ScarID,RejectionComments):
        objFilter.NavigateToSCAR(ScarID)
        objActions.clickElement(QET.Reject_button_xpath, "xpath")
        objActions.enterText(QET.RejectionComments_WebEdit_xpath, "xpath", RejectionComments)
        objActions.clickElement(QET.Confirm_button_xpath, "xpath")
        objCommon.capture_screenshot("Containment Actions Rejected")
        assert(objActions.AssertObjectExists(QET.RCCARejected_WebElement_xpath,"xpath"))




    def ValidateRCCAExtensionDate(self,intTotalDays):
        strActDate = objCommon.ModifyDate("add", intTotalDays+1)
        print("Actual Date to be displayed:" + strActDate)
        time.sleep(2)
        strECDDate = objActions.getText(QET.ECDDate_WebElement_xpath, "xpath")
        strExpDate = strECDDate.split(":")[1]
        print("Date displayed in application:" + strExpDate)
        if strActDate == strExpDate:
            print("RCCA extension date is auto set to: "+strActDate)
        else:
            print("RCCA extension date is set to: "+strActDate+" instead of setting it to :"+strExpDate)
        assert strActDate == strExpDate


    def ValidateRCCARejection_ECD(self):
        time.sleep(2)
        strActDate = objCommon.ModifyDateWithOutWeekends("add", 10)
        print("Actual Date to be displayed:" + strActDate)
        time.sleep(2)
        strECDDate = objActions.getText(QET.ECDDate_WebElement_xpath, "xpath")
        strExpDate = strECDDate.split(":")[1]
        print("Date displayed in application:" + strExpDate)
        if strActDate == strExpDate:
            print("ECD date auto set to 10 days from the day of creation of SCAR, that is on: " + strActDate)
        else:
            print("Could not auto set the ECD date to 10 days from the day of creation of SCAR,that is:"+ strActDate+" instead the application displays:"+strExpDate)
        assert strActDate == strExpDate



    def User_RCCA_RejectRCCA(self,ScarID,RejectionComments):
        objFilter.NavigateToSCAR(ScarID)
        objActions.clickElement(QET.Reject_button_xpath, "xpath")
        objActions.enterText(QET.RejectionComments_WebEdit_xpath, "xpath", RejectionComments)
        objActions.clickElement(QET.Confirm_button_xpath, "xpath")
        objCommon.capture_screenshot("RCCA Actions Rejected")
        assert(objActions.AssertObjectExists(QET.RCCAActionsRejected_Webelement_xpath,"xpath"))
        strActDate=objCommon.ModifyDateWithOutWeekends("add",10)
        print("Actual Date to be displayed:"+strActDate)
        time.sleep(2)
        strECDDate=objActions.getText(QET.ECDDate_WebElement_xpath,"xpath")
        strExpDate=strECDDate.split(":")[1]
        print("Date displayed in application:"+strExpDate)
        if strActDate==strExpDate:
            print("RCCA ECD date is auto set to 10 days from date of rejection")
        else:
            print("RCCA ECD date is not auto set to 10 days from date of rejection")
        assert strActDate==strExpDate


    def User_RejectValidation(self,ScarID,RejectionComments):
        objFilter.NavigateToSCAR(ScarID)
        objActions.clickElement(QET.Reject_button_xpath, "xpath")
        objActions.enterText(QET.RejectionComments_WebEdit_xpath, "xpath", RejectionComments)
        objActions.clickElement(QET.Confirm_button_xpath, "xpath")
        time.sleep(2)
        assert(objActions.AssertObjectExists(QET.ValidationRejected_WebElement_xpath,"xpath"))
        assert(objActions.AssertObjectExists(QET.ScarClosed_WebElement_xpath,"xpath"))
        objCommon.capture_screenshot("Validation Actions Rejected")
        strSCARText=objActions.getText(QET.NewSCARID_WebElement_xpath,"xpath")
        print(strSCARText)


    def User_AssignValidationToSupplier(self,ScarID):
            objFilter.NavigateToSCAR(ScarID)
            objActions.clickElement(QET.Approve_button_xpath, "xpath")
            objActions.clickElement(QET.Confirm_button_xpath, "xpath")
            objActions.clickElement(QET.AssignToSupplier_Button_xpath, "xpath")
            time.sleep(2)
            objCommon.capture_screenshot("Juniper assigned Validation deliverables to Supplier")
            assert(objActions.AssertObjectExists(QET.JnAssignedValidationToSupplier_WebElement_xpath,"xpath"))


    def User_ApproveScar(self,ScarID):
        objFilter.NavigateToSCAR(ScarID)
        objActions.clickElement(QET.Approve_button_xpath, "xpath")
        objActions.clickElement(QET.Confirm_button_xpath, "xpath")
        time.sleep(5)
        objCommon.capture_screenshot("SCAR Closed")
        assert(objActions.AssertObjectExists(QET.ScarClosed_WebElement_xpath, "xpath"))

















