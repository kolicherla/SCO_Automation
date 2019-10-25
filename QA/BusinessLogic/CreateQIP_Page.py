from QA.PageObjects.Test_Locators import QET
from QA.Utilities.PerformAction import PerformActions
from QA.Utilities.CommonLib import CommonFunctions
from QA.Base.Config import MyConfigFiles
from QA.BusinessLogic.Filter_Page import Filter
from QA.BusinessLogic.Home_Page import Home

import time

class createQIP_Page():
    global objCommon, objActions,objHome,objFilter
    objCommon = CommonFunctions()
    objActions = PerformActions()
    objFilter = Filter()
    objHome = Home()

    #Mehtod for create QIP
    def CreateQIP(Self,ProblemDescription,UserGroup,Supplier,Contact,Escalation,Jn_Escalation):
        objDic = dict();
        objHome.ClickQIPButton()
        time.sleep(2)
        objFilter.ClickCreate()
        objActions.enterText(QET.ProblemDescription_WebEdit_xpath, "xpath", ProblemDescription)
        time.sleep(2)
        objActions.selectDropdown(QET.QET_UserGroup_SelectBox_xpath, "xpath", "value", UserGroup)
        time.sleep(2)
        objActions.selectDropdown(QET.Supplier_SelectBox_xpath, "xpath", "visibletext", Supplier)
        objActions.selectDropdown(QET.Contact_SelectBox_xpath, "xpath", "visibletext", Contact)
        objActions.selectDropdown(QET.Escalation_SelectBox_xpath, "xpath", "visibletext", Escalation)
        objActions.enterText(QET.Escalation_WebEdit_xpath, "xpath", Jn_Escalation)
        time.sleep(2)
        objActions.clickElement("//span[text()='" + Jn_Escalation + "']", "xpath")
        time.sleep(2)
        objActions.clickElement(QET.CreateScar_button_xpath, "xpath")
        objCommon.capture_screenshot('QIP Created Successfully')
        strQIPID = objActions.getText(QET.QETID_WebElement_xpath, "xpath")
        print("QIP Created successfully with ID:" + strQIPID)
        assert (objActions.AssertObjectExists(QET.QIP_Created_Timeline, "xpath"))
        strQIPCreateddate=objCommon.GetCurrentDate()
        strURL = objActions.getURL()
        objDic['URL'] = strURL
        objDic['QIPID'] = strQIPID
        objDic['QIPCD'] = strQIPCreateddate
        return objDic

# Issuing the QIP
    def IssueQIP(self):
        # time.sleep(2)
        objActions.clickElement(QET.IssueQIP_button_xpath, "xpath")
        assert (objActions.AssertObjectExists(QET.QIPIssued_WebElement_xpath, "xpath"))
        objCommon.capture_screenshot("QIP Issued Successfully")


    def User_ApproveQIP(self,QIPID):
        objFilter.NavigateToQIP(QIPID)
        objActions.clickElement(QET.Approve_button_xpath, "xpath")
        objActions.clickElement(QET.Confirm_button_xpath, "xpath")
        objCommon.capture_screenshot("Containment plan approved")
        assert(objActions.AssertObjectExists(QET.JnApprovedContainmentplan_webElement_xpath, "xpath"))



    def User_RejectQIP(self,QIPID,RejectionComments):
        objFilter.NavigateToQIP(QIPID)
        objActions.clickElement(QET.Reject_button_xpath, "xpath")
        objActions.enterText(QET.RejectionComments_WebEdit_xpath,"xpath",RejectionComments)
        objActions.clickElement(QET.Confirm_button_xpath,"xpath")
        objCommon.capture_screenshot("Containment plan Rejected")
        assert (objActions.AssertObjectExists(QET.RejectedContainmentplan_WebElement_xpath,"xpath"))

    def User_RejectRCCA(self,QIPID,RejectionComments,strTimestatus):
        objFilter.NavigateToQIP(QIPID)
        objActions.clickElement(QET.Reject_button_xpath, "xpath")
        objActions.enterText(QET.RejectionComments_WebEdit_xpath, "xpath", RejectionComments)
        objActions.clickElement(QET.Confirm_button_xpath, "xpath")
        if strTimestatus == "RCCA actions rejected":
            assert (objActions.AssertObjectExists(QET.RCCAActionsRejected_Webelement_xpath, "xpath"))
            RCCA_reject_ECD = objActions.getText(QET.ECDDate_WebElement_xpath, "xpath")
            objCommon.capture_screenshot("RCCA Actions Rejected")
        else:
            objActions.getText(QET.QIP_RCCAPlanRejected_WebElement_xpath, "xpath")
            assert (objActions.AssertObjectExists(QET.QIP_RCCAPlanRejected_WebElement_xpath, "xpath"))
            objCommon.capture_screenshot("RCCA Plan rejected")

    def User_AssignValidationToSupplier(self,QIPID):
            objFilter.NavigateToQIP(QIPID)
            objActions.clickElement(QET.Approve_button_xpath, "xpath")
            objActions.clickElement(QET.Confirm_button_xpath, "xpath")
            # objActions.clickElement(QET.AssignToSupplier_Button_xpath, "xpath")
            time.sleep(2)
            objCommon.capture_screenshot("Pending Completion of Containment and RCCA Actions from Supplier")
            assert(objActions.AssertObjectExists(QET.jn_RCCAPlanapproved_WebElement_xapth,"xpath"))

    def User_ApproveQip(self,QIPID):
        objFilter.NavigateToQIP(QIPID)
        objActions.clickElement(QET.Approve_button_xpath, "xpath")
        objActions.clickElement(QET.Confirm_button_xpath, "xpath")
        time.sleep(5)
        objCommon.capture_screenshot("Juniper Approved Containment and RCCA Actions")
        assert(objActions.AssertObjectExists(QET.Jn_Approved_CandRCCAActions_WebElement_xpath, "xpath"))


    def ValidateRCCAExtensionDate(self,intTotalDays,QIPID):
        objFilter.NavigateToQIP(QIPID)
        time.sleep(2)
        objActions.clickElement(QET.QIP_BacktoRCCA_WebElement, "xpath")
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

    def ValidateRCCAExtensionandECDDates(self,QIPID):
        objFilter.NavigateToQIP(QIPID)
        time.sleep(2)
        objActions.clickElement(QET.QIP_BacktoRCCA_WebElement, "xpath")
        strECDText = objActions.getText(QET.ECDDate_WebElement_xpath, "xpath")
        strActDate=strECDText.split(":")[1]
        # print("Actual Date to be displayed:" + strActDate)
        time.sleep(2)
        strECDDate = objActions.getText(QET.ECDDate_WebElement_xpath, "xpath")
        strExpDate = strECDDate.split(":")[1]
        # print("Date displayed in application:" + strExpDate)
        if strActDate == strExpDate:
            print("RCCA ECD date set and same as : "+strExpDate+" RCCA extension date:"+strActDate)
        else:
            print("RCCA extension date is set to: "+strActDate+" instead of setting it to :"+strExpDate)
        assert strActDate == strExpDate

    def ValidateRCCARejection_ECD(self):
        time.sleep(2)
        strActDate = objCommon.ModifyDateWithOutWeekends("add", 5)
        print("Actual Date to be displayed:" + strActDate)
        time.sleep(2)
        strECDDate = objActions.getText(QET.ECDDate_WebElement_xpath, "xpath")
        strExpDate = strECDDate.split(":")[1]
        print("Date displayed in application:" + strExpDate)
        if strActDate == strExpDate:
            print("ECD date auto set to 5 days from the day of creation of QIP, that is on: " + strActDate)
        else:
            print("Could not auto set the ECD date to 5 days from the day of creation of QIP,that is:"+ strActDate+" instead the application displays:"+strExpDate)
        assert strActDate == strExpDate

    def SubmitforApproval(self,QIPID):
        objFilter.NavigateToQIP(QIPID)
        objActions.clickElement(QET.SubmitForApproval_Button_xpath, "xpath")
        time.sleep(2)
        objCommon.capture_screenshot("Pending Juniper Approval of Containment and RCCA")
        assert (objActions.AssertObjectExists(QET.Supplier_CRCCAAction_Sub_WebElement_xpath, "xpath"))


    def User_ApproveQIPCLosed(self,QIPID):
        # objFilter.NavigateToQIP(QIPID)
        # objActions.clickElement(QET.Approve_button_xpath, "xpath")
        # objActions.clickElement(QET.Confirm_button_xpath, "xpath")
        time.sleep(5)
        objCommon.capture_screenshot("QIP Closed")
        assert(objActions.AssertObjectExists(QET.QIPClosed_WebElement_xpath, "xpath"))

    def User_RejectValidation(self,QIPID,RejectionComments):
        objFilter.NavigateToQIP(QIPID)
        objActions.clickElement(QET.QIP_Reject_button_xpath, "xpath")
        objActions.enterText(QET.RejectionComments_WebEdit_xpath, "xpath", RejectionComments)
        objActions.clickElement(QET.Confirm_button_xpath, "xpath")
        time.sleep(2)
        assert(objActions.AssertObjectExists(QET.QIP_RejectClosed_button_xpath,"xpath"))
        objCommon.capture_screenshot("QIP Rejected and Closed")
        # strSCARText=objActions.getText(QET.NewQIPID_WebElement_xpath,"xpath")
        # print(strSCARText)

       # ECD Validation for after QIP issued
    def ValidateContainment_ECD(self,strQIPCreateddate):
        time.sleep(2)
        strActDate = objCommon.ModifyDateWithOutWeekends("add", 7)
        print("Actual Date to be displayed:" + strActDate)
        time.sleep(2)
        strECDDate = objActions.getText(QET.ECDDate_WebElement_xpath, "xpath")
        strExpDate = strECDDate.split(":")[1]
        print("Date displayed in application:" + strExpDate)
        if strActDate == strExpDate:
            print("QIP created Date is : " +strQIPCreateddate + "ECD date auto set to 7 days from the day of creation of QIP, that is on: " + strActDate)
        else:
            print("Could not auto set the ECD date to 7 days from the day of creation of QIP,that is:" + strActDate + " instead the application displays:" + strExpDate)
        assert strActDate == strExpDate

    # ECD Validation for after Containment plan Appoved.

    def Validate_RCCA_ECD_CPApproved(self):
        time.sleep(2)
        strActDate = objCommon.ModifyMonth("add", 1)
        print("Actual Date to be displayed:" + strActDate)
        time.sleep(2)
        strECDDate = objActions.getText(QET.ECDDate_WebElement_xpath, "xpath")
        strExpDate = strECDDate.split(":")[1]
        print("Date displayed in application:" + strExpDate)
        if strActDate == strExpDate:
            print("ECD date  set to 1 Month from Appoved Contaiment plan that is on: " + strActDate)
        else:
            print("Could not  set the ECD date to 1 Monthfrom the Appoved Contaiment plan,that is:" + strActDate + " instead the application displays:" + strExpDate)
        assert strActDate == strExpDate


    def ValidateRCCA_Extn_Rejection_ECD(self):
        time.sleep(2)
        RCCA_reject_ECD = objActions.getText(QET.ECDDate_WebElement_xpath, "xpath")
        RCCA_Plan_ECD = objActions.getText(QET.ECDDate_WebElement_xpath, "xpath")
        if RCCA_reject_ECD == RCCA_Plan_ECD:
           print("previously selected RCCA ECD date will be retained: " + RCCA_reject_ECD)
        else:
           print("not displayed previously selected RCCA ECD date ")
        assert RCCA_reject_ECD == RCCA_Plan_ECD



    def User_RCCA_RejectRCCA(self,QIPID,RejectionComments):
        objFilter.NavigateToQIP(QIPID)
        objActions.clickElement(QET.Reject_button_xpath, "xpath")
        objActions.enterText(QET.RejectionComments_WebEdit_xpath, "xpath", RejectionComments)
        objActions.clickElement(QET.Confirm_button_xpath, "xpath")
        objCommon.capture_screenshot("RCCA Actions Rejected")
        time.sleep(2)
        assert(objActions.AssertObjectExists(QET.QIP_RCCAPlanRejected_WebElement_xpath,"xpath"))
        strActDate=objCommon.ModifyDateWithOutWeekends("add",5)
        print("Actual Date to be displayed:"+strActDate)
        time.sleep(2)
        strECDDate=objActions.getText(QET.ECDDate_WebElement_xpath,"xpath")
        strExpDate=strECDDate.split(":")[1]
        print("Date displayed in application:"+strExpDate)
        if strActDate==strExpDate:
            print("RCCA ECD date is auto set to 5 days from date of rejection")
        else:
            print("RCCA ECD date is not auto set to 5 days from date of rejection")
        assert strActDate==strExpDate



