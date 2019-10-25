from QA.BusinessLogic.CreateQIP_Page import createQIP_Page
from QA.BusinessLogic.Login_Page import login_Page
from QA.Utilities.CommonLib import CommonFunctions
from QA.BusinessLogic.EditQIP_Page import EditQIPs
from QA.BusinessLogic.Supplier_QIP_Page import SupplierQIP
import pytest

class Test_QIP():
    global objLogin, objCreate, objCommon, objEditQIP, objSupplier
    objLogin=login_Page()
    objCreate=createQIP_Page()
    objCommon = CommonFunctions()
    objEditQIP = EditQIPs()
    objSupplier = SupplierQIP()

    @pytest.mark.sanity
    @pytest.mark.P3
    # @pytest.mark.dependency()
    def test_TC001_QIP_CreatingQIP(self, setup, TestData):
        objLogin.QET_Login(TestData['UserName'], TestData['Password'])
        objCreate.CreateQIP(TestData['ProblemDescription'], TestData['UserGroup'], TestData['Supplier'], TestData['Contact']
                            , TestData['Escalation'], TestData['Jn_Escalation'])

        objLogin.QET_LogOut()

    @pytest.mark.P3
    @pytest.mark.regression
    @pytest.mark.dependency()
    def test_TC002_QIP_IssueQIP(self, setup, TestData):
        objLogin.QET_Login(TestData['UserName'], TestData['Password'])
        strData = objCreate.CreateQIP(TestData['ProblemDescription'], TestData['UserGroup'], TestData['Supplier']
                                           , TestData['Contact'], TestData['Escalation'], TestData['Jn_Escalation'])
        objCreate.IssueQIP()
        objCreate.ValidateContainment_ECD(strData['QIPCD'])
        objLogin.QET_LogOut()
        return strData

    @pytest.mark.P3
    @pytest.mark.regression
    def test_TC003_QIP_EditQIP(self, setup, TestData):
        objLogin.QET_Login(TestData['UserName'], TestData['Password'])
        objCreate.CreateQIP(TestData['ProblemDescription'], TestData['UserGroup'], TestData['Supplier']
                                 , TestData['Contact'], TestData['Escalation'], TestData['Jn_Escalation'])
        objCreate.IssueQIP()
        objEditQIP.EditQIP(TestData['UpdatedProblemDescription'],TestData['JuniperWatchList'],TestData['SupplierQIPteam']
                              , TestData['JuniperQIPTeam'],TestData['SupplierWatchList'])
        objLogin.QET_LogOut()

    @pytest.mark.P3
    @pytest.mark.regression
    #@pytest.mark.dependency(depends=["Test_QIP::test_TC002_QIP_IssueQIP"])
    def test_TC004_QIP_ContainmentPhase_EditAction(self, setup, TestData):
        strData = self.test_TC002_QIP_IssueQIP(setup, TestData)
        # Creating containment and Editing it
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['Supplier_UserName'], TestData['Supplier_Password'])
        objSupplier.Supplier_EditContainment(strData['QIPID'], TestData['CA_Title'], TestData['CA_Description'],TestData['CA_UpdatedTitle'])
        objLogin.QET_LogOut()

    @pytest.mark.regression
    @pytest.mark.P2
    #@pytest.mark.dependency(depends=["Test_SCAR::test_TC002_SCAR_IssueSCAR"])
    def test_TC005_QIP_ContainmentPhase_DeleteAction(self, setup, TestData):
        # Creating and Issuing a QIP
        strData = self.test_TC002_QIP_IssueQIP(setup, TestData)
        # Adding Containment using Supplier Login Credentials
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['Supplier_UserName'], TestData['Supplier_Password'])
        objSupplier.Supplier_Containment_DeleteAction(strData['QIPID'], TestData['CA_Title'], TestData['CA_Description'])
        objLogin.QET_LogOut()

    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    # @pytest.mark.dependency(depends=["Test_SCAR::test_TC002_QIP_IssueSCAR"])
    def test_TC006_QIP_ApproveContainmentPhase(self, setup, TestData):
        # Creating and Issuing a SCAR
        strData = self.test_TC002_QIP_IssueQIP(setup, TestData)
        # Adding Containment using Supplier Login Credentials
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['Supplier_UserName'], TestData['Supplier_Password'])
        objSupplier.Supplier_AddingContainment(strData['QIPID'], TestData['CA_Title'], TestData['CA_Description'], TestData['Supplier_QIPteam'])
        objLogin.QET_LogOut()
        objCommon.CloseBrowser()

        # Login with User credentials to approve the SCAR
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['UserName'], TestData['Password'])
        objCreate.User_ApproveQIP(strData['QIPID'])
        objCreate.Validate_RCCA_ECD_CPApproved()
        objLogin.QET_LogOut()
        return strData

    @pytest.mark.regression
    @pytest.mark.P2
    @pytest.mark.dependency()
    # @pytest.mark.dependency(depends=["Test_SCAR::test_TC002_QIP_IssueQIP"])
    def test_TC007_QIP_RejectContainmentPhase(self, setup, TestData):
        # Creating and Issuing a QIP
        strData = self.test_TC002_QIP_IssueQIP(setup, TestData)

        # Adding Containment using Supplier Login Credentials
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['Supplier_UserName'], TestData['Supplier_Password'])
        objSupplier.Supplier_AddingContainment(strData['QIPID'], TestData['CA_Title'], TestData['CA_Description'],TestData['Supplier_QIPteam'])
        objLogin.QET_LogOut()
        objCommon.CloseBrowser()

        # Login with User credentials to approve the QIP
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['UserName'], TestData['Password'])
        objCreate.User_RejectQIP(strData['QIPID'], TestData['RejectionComments'])
        objLogin.QET_LogOut()

    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    # @pytest.mark.dependency(depends=["Test_SCAR::test_TC006_QIP_ApproveContainmentPhase"])
    def test_TC008_QIP_RCCAPhase_EditAction(self, setup, TestData):
        strData = self.test_TC006_QIP_ApproveContainmentPhase(setup, TestData)
        # Login back to Supplier to create RCCA
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['Supplier_UserName'], TestData['Supplier_Password'])
        objSupplier.Supplier_EditRCCA(strData['QIPID'], TestData['CA_Title'], TestData['CA_Description'],TestData['CA_UpdatedTitle'])
        objLogin.QET_LogOut()

    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    # @pytest.mark.dependency(depends=["Test_QIP::test_TC006_QIP_ApproveContainmentPhase"])
    def test_TC009_QIP_RCCAPhase_DeleteAction(self, setup, TestData):
        strData = self.test_TC006_QIP_ApproveContainmentPhase(setup, TestData)
        # Login back to Supplier to create RCCA
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['Supplier_UserName'], TestData['Supplier_Password'])
        objSupplier.Supplier_RCCA_DeleteAction(strData['QIPID'], TestData['CA_Title'], TestData['CA_Description'])
        objLogin.QET_LogOut()

    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    # @pytest.mark.dependency(depends=["Test_QIP::test_TC006_QIP_ApproveContainmentPhase"])
    def test_TC010_QIP_ApproveRCCAPhase(self, setup, TestData):
        strData = self.test_TC006_QIP_ApproveContainmentPhase(setup, TestData)
        # Login back to Supplier to create RCCA
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['Supplier_UserName'], TestData['Supplier_Password'])
        objSupplier.Supplier_AddRCCA(strData['QIPID'], TestData['CA_Title'], TestData['CA_Description'])
        objLogin.QET_LogOut()
        objCommon.CloseBrowser()

        # Login with User to Approve
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['UserName'], TestData['Password'])
        objCreate.User_AssignValidationToSupplier(strData['QIPID'])
        objLogin.QET_LogOut()
        return strData

    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    # @pytest.mark.dependency(depends=["Test_QIP::test_TC002_QIP_IssueQIP"])
    def test_TC011_QIP_RCCAPhase_RequestForExtension(self, setup, TestData):
        # Login with User to  Approve RCCA Plan
        strData = self.test_TC010_QIP_ApproveRCCAPhase(setup, TestData)
        # Login Back to Supplier to RequestForExtension
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['Supplier_UserName'], TestData['Supplier_Password'])
        objSupplier.SupplierRequestExtension(strData['QIPID'],TestData['ExtensionDays'], TestData['ExtensionReason'])
        objLogin.QET_LogOut()
        # approve with user credentials
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['UserName'], TestData['Password'])
        objCreate.User_ApproveQip(strData['QIPID'])
        objLogin.QET_LogOut()

        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['Supplier_UserName'], TestData['Supplier_Password'])
        objCreate.ValidateRCCAExtensionandECDDates(strData['QIPID'])
        objLogin.QET_LogOut()

    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    # @pytest.mark.dependency(depends=["Test_QIP::test_TC002_QIP_IssueQIP"])
    def test_TC012_QIP_RCCAPhase_Reject_RequestForExtension(self, setup, TestData):
        # Creating and Issuing a SCAR
        strData = self.test_TC010_QIP_ApproveRCCAPhase(setup, TestData)
        # Login Back to Supplier to RequestForExtension
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['Supplier_UserName'], TestData['Supplier_Password'])
        objSupplier.SupplierRequestExtension(strData['QIPID'], TestData['ExtensionDays'], TestData['ExtensionReason'])
        objLogin.QET_LogOut()
        # approve with user credentials
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['UserName'], TestData['Password'])
        objCreate.User_RejectRCCA(strData['QIPID'], TestData['RejectionComments'],'RCCA actions rejected')
        objCreate.ValidateRCCA_Extn_Rejection_ECD()
        objLogin.QET_LogOut()

    @pytest.mark.regression
    @pytest.mark.P1
    # @pytest.mark.dependency(depends=["Test_SCAR::test_TC006_SCAR_ApproveContainmentPhase"])
    def test_TC013_QIP_RCCAPhase_RejectRCCA(self, setup, TestData):
        strData = self.test_TC006_QIP_ApproveContainmentPhase(setup, TestData)
        # Login back to Supplier to create RCCA
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['Supplier_UserName'], TestData['Supplier_Password'])
        objSupplier.Supplier_AddRCCA(strData['QIPID'], TestData['CA_Title'], TestData['CA_Description'])
        objLogin.QET_LogOut()
        objCommon.CloseBrowser()

        # Login with User to Approve
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['UserName'], TestData['Password'])
        objCreate.User_RCCA_RejectRCCA(strData['QIPID'], TestData['RejectionComments'])
        # objCreate.ValidateRCCARejection_ECD()
        objLogin.QET_LogOut()

    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    # @pytest.mark.dependency(depends=["Test_QIP::test_TC010_QIP_ApproveRCCAPhase"])
    def test_TC014_QIP_ValidationPhase_EditAction(self, setup, TestData):
        strData = self.test_TC010_QIP_ApproveRCCAPhase(setup, TestData)
        # Login with Supplier to Sunbmit for Approval
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['Supplier_UserName'], TestData['Supplier_Password'])
        objCreate.SubmitforApproval(strData['QIPID'])
        objLogin.QET_LogOut()
        #Login with Juniper to Add Deliverables
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['UserName'], TestData['Password'])
        objCreate.User_ApproveQip(strData['QIPID'])
        objSupplier.Supplier_EditDeliverables(strData['QIPID'], TestData['CA_Title'], TestData['CA_Description'],TestData['CA_UpdatedTitle'])
        objLogin.QET_LogOut()

    @pytest.mark.regression
    @pytest.mark.P2
    @pytest.mark.dependency()
    # @pytest.mark.dependency(depends=["Test_SCAR::test_TC010_SCAR_ApproveRCCAPhase"])
    def test_TC015_QIP_ValidationPhase_DeleteAction(self, setup, TestData):
        strData = self.test_TC010_QIP_ApproveRCCAPhase(setup, TestData)
        # Login with Supplier to Sunbmit for Approval
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['Supplier_UserName'], TestData['Supplier_Password'])
        objCreate.SubmitforApproval(strData['QIPID'])
        objLogin.QET_LogOut()
        # Login with Juniper to Add Deliverables
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['UserName'], TestData['Password'])
        objCreate.User_ApproveQip(strData['QIPID'])
        objSupplier.Supplier_Validation_DeleteAction(strData['QIPID'], TestData['CA_Title'], TestData['CA_Description'])
        objLogin.QET_LogOut()

    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    # @pytest.mark.dependency(depends=["Test_SCAR::test_TC010_SCAR_ApproveRCCAPhase"])
    def test_TC016_QIP_ApproveValidationPhase(self, setup, TestData):
        strData = self.test_TC010_QIP_ApproveRCCAPhase(setup, TestData)
        # Login with Supplier to Sunbmit for Approval
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['Supplier_UserName'], TestData['Supplier_Password'])
        objCreate.SubmitforApproval(strData['QIPID'])
        objLogin.QET_LogOut()
        # Login with Juniper to Add Deliverables
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['UserName'], TestData['Password'])
        objCreate.User_ApproveQip(strData['QIPID'])
        objSupplier.Supplier_AddDeliverables(strData['QIPID'], TestData['CA_Title'], TestData['CA_Description'])
        objCreate.User_ApproveQIPCLosed(strData['QIPID'])
        objLogin.QET_LogOut()
        objCommon.CloseBrowser()

        # Login with Juniper to Approve
        # objCommon.LaunchBrowser(strData['URL'])
        # objLogin.QET_Login(TestData['UserName'], TestData['Password'])
        # objCreate.User_ApproveQIPCLosed(strData['QIPID'])
        # objLogin.QET_LogOut()

    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    # @pytest.mark.dependency(depends=["Test_SCAR::test_TC010_SCAR_ApproveRCCAPhase"])
    def test_TC017_QIP_ValidationPhase_RequestForExtension(self, setup, TestData):
        strData = self.test_TC010_QIP_ApproveRCCAPhase(setup, TestData)
        # Login with Supplier to Add Deliverables
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['Supplier_UserName'], TestData['Supplier_Password'])
        objCreate.SubmitforApproval(strData['QIPID'])
        objLogin.QET_LogOut()
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['UserName'], TestData['Password'])
        objCreate.User_ApproveQip(strData['QIPID'])
        objSupplier.Supplier_AddDeliverables_RequestExtension(strData['QIPID'], TestData['CA_Title'],TestData['CA_Description'])
        objSupplier.User_Extend_Validation(strData['QIPID'],TestData['ExtensionDays'], TestData['ExtensionReason'])
        objLogin.QET_LogOut()


    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    # @pytest.mark.dependency(depends=["Test_SCAR::test_TC010_SCAR_ApproveRCCAPhase"])
    def test_TC018_QIP_ValidationPhase_Reject_RequestForExtension(self, setup, TestData):
        strData = self.test_TC010_QIP_ApproveRCCAPhase(setup, TestData)
        # Login with Supplier to Add Deliverables
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['Supplier_UserName'], TestData['Supplier_Password'])
        objSupplier.Supplier_AddDeliverables_RequestExtension(strData['QIPID'], TestData['CA_Title'],
                                                              TestData['CA_Description'])
        objSupplier.SupplierRequestExtension(TestData['ExtensionDays'], TestData['ExtensionReason'])
        objLogin.QET_LogOut()

        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['UserName'], TestData['Password'])
        objCreate.User_RejectValidation(strData['QIPID'], TestData['RejectionComments'])
        objLogin.QET_LogOut()

    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    # @pytest.mark.dependency(depends=["Test_SCAR::test_TC010_SCAR_ApproveRCCAPhase"])
    def test_TC019_QIP_ValidationPhase_Reject(self, setup, TestData):
        strData = self.test_TC010_QIP_ApproveRCCAPhase(setup, TestData)
        # Login with Supplier to Add Deliverables
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['Supplier_UserName'], TestData['Supplier_Password'])
        objCreate.SubmitforApproval(strData['QIPID'])
        objLogin.QET_LogOut()
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['UserName'], TestData['Password'])
        objCreate.User_ApproveQip(strData['QIPID'])
        objCreate.User_RejectValidation(strData['QIPID'], TestData['RejectionComments'])
        objLogin.QET_LogOut()
        # objCommon.CloseBrowser()

