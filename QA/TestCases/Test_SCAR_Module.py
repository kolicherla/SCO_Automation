from QA.BusinessLogic.CreateSCAR_Page import createSCAR_Page
from QA.BusinessLogic.Login_Page import login_Page
from QA.Utilities.CommonLib import CommonFunctions
from QA.BusinessLogic.EditSCAR_Page import EditSCARs
from QA.BusinessLogic.Supplier_SCAR_Page import SupplierSCAR
import pytest


class Test_SCAR():
    global objLogin, objCreateScar, objCommon, objEditSCAR, objSupplier
    objLogin=login_Page()
    objCreateScar=createSCAR_Page()
    objCommon = CommonFunctions()
    objEditSCAR=EditSCARs()
    objSupplier=SupplierSCAR()


    @pytest.mark.dependency()
    @pytest.mark.regression
    @pytest.mark.P1
    def test_TC001_SCAR_CreatingSCAR(self, setup, TestData):
        # Creating and Issuing a SCAR
        objLogin.QET_Login(TestData['UserName'], TestData['Password'])
        objCreateScar.CreateSCAR(TestData['ProblemDescription'], TestData['AffectedPart'],
                                           TestData['UserGroup'], TestData['Supplier']
                                           , TestData['Contact'], TestData['Escalation'], TestData['Jn_Escalation'],
                                           TestData['JnWatchlist'])
        objLogin.QET_LogOut()



    @pytest.mark.P1
    @pytest.mark.regression
    @pytest.mark.dependency()
    def test_TC002_SCAR_IssueSCAR(self, setup, TestData):
        objLogin.QET_Login(TestData['UserName'], TestData['Password'])
        strData=objCreateScar.CreateSCAR(TestData['ProblemDescription'], TestData['AffectedPart'],
                                 TestData['UserGroup'], TestData['Supplier']
                                 , TestData['Contact'], TestData['Escalation'], TestData['Jn_Escalation'],
                                 TestData['JnWatchlist'])
        objCreateScar.IssueSCAR()
        objLogin.QET_LogOut()
        return strData



    @pytest.mark.P1
    @pytest.mark.regression
    def test_TC003_SCAR_EditSCAR(self, setup, TestData):
        objLogin.QET_Login(TestData['UserName'], TestData['Password'])
        objCreateScar.CreateSCAR(TestData['ProblemDescription'], TestData['AffectedPart'],
                                           TestData['UserGroup'], TestData['Supplier']
                                           , TestData['Contact'], TestData['Escalation'], TestData['Jn_Escalation'],
                                           TestData['JnWatchlist'])
        objCreateScar.IssueSCAR()
        objEditSCAR.EditSCAR(TestData['UpdatedProblemDescription'])
        objLogin.QET_LogOut()



    @pytest.mark.P2
    @pytest.mark.regression
    @pytest.mark.dependency(depends=["Test_SCAR::test_TC002_SCAR_IssueSCAR"])
    def test_TC004_SCAR_ContainmentPhase_EditAction(self, setup, TestData):
        strData = self.test_TC002_SCAR_IssueSCAR(setup, TestData)

        # Creating containment and Editing it
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['Supplier_UserName'], TestData['Supplier_Password'])
        objSupplier.Supplier_EditContainment(strData['ScarID'],TestData['CA_Title'],TestData['CA_Description'],TestData['CA_UpdatedTitle'])
        objLogin.QET_LogOut()


    @pytest.mark.regression
    @pytest.mark.P2
    @pytest.mark.dependency(depends=["Test_SCAR::test_TC002_SCAR_IssueSCAR"])
    def test_TC005_SCAR_ContainmentPhase_DeleteAction(self, setup, TestData):
        # Creating and Issuing a SCAR
        strData = self.test_TC002_SCAR_IssueSCAR(setup,TestData)

        # Adding Containment using Supplier Login Credentials
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['Supplier_UserName'], TestData['Supplier_Password'])
        objSupplier.Supplier_Containment_DeleteAction(strData['ScarID'],TestData['CA_Title'],TestData['CA_Description'])
        objLogin.QET_LogOut()



    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    #@pytest.mark.dependency(depends=["Test_SCAR::test_TC002_SCAR_IssueSCAR"])
    def test_TC006_SCAR_ApproveContainmentPhase(self,setup,TestData):
        #Creating and Issuing a SCAR
        strData = self.test_TC002_SCAR_IssueSCAR(setup, TestData)
        #Adding Containment using Supplier Login Credentials
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['Supplier_UserName'],TestData['Supplier_Password'])
        objSupplier.Supplier_AddingContainment(strData['ScarID'],TestData['CA_Title'],TestData['CA_Description'])
        objLogin.QET_LogOut()
        objCommon.CloseBrowser()

        #Login with User credentials to approve the SCAR
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['UserName'],TestData['Password'])
        objCreateScar.User_ApproveSCAR(strData['ScarID'])
        objLogin.QET_LogOut()
        return strData



    @pytest.mark.regression
    @pytest.mark.P2
    @pytest.mark.dependency()
    @pytest.mark.dependency(depends=["Test_SCAR::test_TC002_SCAR_IssueSCAR"])
    def test_TC007_SCAR_RejectContainmentPhase(self, setup, TestData):
        # Creating and Issuing a SCAR
        strData = self.test_TC002_SCAR_IssueSCAR(setup, TestData)

        # Adding Containment using Supplier Login Credentials
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['Supplier_UserName'], TestData['Supplier_Password'])
        objSupplier.Supplier_AddingContainment(strData['ScarID'], TestData['CA_Title'], TestData['CA_Description'])
        objLogin.QET_LogOut()
        objCommon.CloseBrowser()

        # Login with User credentials to approve the SCAR
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['UserName'], TestData['Password'])
        objCreateScar.User_RejectSCAR(strData['ScarID'], TestData['RejectionComments'])
        objLogin.QET_LogOut()



    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    @pytest.mark.dependency(depends=["Test_SCAR::test_TC006_SCAR_ApproveContainmentPhase"])
    def test_TC008_SCAR_RCCAPhase_EditAction(self, setup, TestData):
        strData = self.test_TC006_SCAR_ApproveContainmentPhase(setup, TestData)
        # Login back to Supplier to create RCCA
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['Supplier_UserName'], TestData['Supplier_Password'])
        objSupplier.Supplier_EditRCCA(strData['ScarID'],TestData['CA_Title'],TestData['CA_Description'], TestData['CA_UpdatedTitle'])
        objLogin.QET_LogOut()



    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    @pytest.mark.dependency(depends=["Test_SCAR::test_TC006_SCAR_ApproveContainmentPhase"])
    def test_TC009_SCAR_RCCAPhase_DeleteAction(self, setup, TestData):
        strData = self.test_TC006_SCAR_ApproveContainmentPhase(setup, TestData)
        # Login back to Supplier to create RCCA
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['Supplier_UserName'], TestData['Supplier_Password'])
        objSupplier.Supplier_RCCA_DeleteAction(strData['ScarID'],TestData['CA_Title'],TestData['CA_Description'])
        objLogin.QET_LogOut()


    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    @pytest.mark.dependency(depends=["Test_SCAR::test_TC006_SCAR_ApproveContainmentPhase"])
    def test_TC010_SCAR_ApproveRCCAPhase(self, setup, TestData):
        strData=self.test_TC006_SCAR_ApproveContainmentPhase(setup,TestData)
        #Login back to Supplier to create RCCA
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['Supplier_UserName'], TestData['Supplier_Password'])
        objSupplier.Supplier_AddRCCA(strData['ScarID'],TestData['CA_Title'],TestData['CA_Description'])
        objLogin.QET_LogOut()
        objCommon.CloseBrowser()

        #Login with User to Approve
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['UserName'], TestData['Password'])
        objCreateScar.User_AssignValidationToSupplier(strData['ScarID'])
        objLogin.QET_LogOut()
        return strData


    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    #@pytest.mark.dependency(depends=["Test_SCAR::test_TC002_SCAR_IssueSCAR"])
    def test_TC011_SCAR_RCCAPhase_RequestForExtension(self, setup, TestData):
        # Creating and Issuing a SCAR
        strData = self.test_TC002_SCAR_IssueSCAR(setup, TestData)

        #Adding Containment using Supplier Login Credentials
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['Supplier_UserName'], TestData['Supplier_Password'])
        objSupplier.Supplier_ECDForRCCA_AddingContainment(strData['ScarID'],TestData['CA_Title'],TestData['CA_Description'],TestData['ECDDays'])
        objLogin.QET_LogOut()
        #approve with user credentials
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['UserName'], TestData['Password'])
        objCreateScar.User_ApproveSCAR(strData['ScarID'])
        objLogin.QET_LogOut()

        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['Supplier_UserName'], TestData['Supplier_Password'])
        objSupplier.Supplier_AddRCCAWithoutSubmit(strData['ScarID'],TestData['CA_Title'],TestData['CA_Description'])
        objSupplier.SupplierRequestExtension(TestData['ExtensionDays'],TestData['ExtensionReason'])
        intTotalDays=TestData['ExtensionDays']+TestData['ECDDays']
        objCreateScar.ValidateRCCAExtensionDate(intTotalDays)
        # objLogin.QET_LogOut()


    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    @pytest.mark.dependency(depends=["Test_SCAR::test_TC002_SCAR_IssueSCAR"])
    def test_TC012_SCAR_RCCAPhase_Reject_RequestForExtension(self, setup, TestData):
        # Creating and Issuing a SCAR
        strData = self.test_TC002_SCAR_IssueSCAR(setup, TestData)

        # Adding Containment using Supplier Login Credentials
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['Supplier_UserName'], TestData['Supplier_Password'])
        objSupplier.Supplier_ECDForRCCA_AddingContainment(strData['ScarID'], TestData['CA_Title'],
                                                            TestData['CA_Description'], TestData['ECDDays'])
        objLogin.QET_LogOut()
        # approve with user credentials
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['UserName'], TestData['Password'])
        objCreateScar.User_ApproveSCAR(strData['ScarID'])
        objLogin.QET_LogOut()

        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['Supplier_UserName'], TestData['Supplier_Password'])
        objSupplier.Supplier_AddRCCAWithoutSubmit(strData['ScarID'], TestData['CA_Title'], TestData['CA_Description'])
        objSupplier.SupplierRequestExtension(TestData['ExtensionDays'], TestData['ExtensionReason'])
        objLogin.QET_LogOut()

        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['UserName'], TestData['Password'])
        objCreateScar.User_RejectRCCA(strData['ScarID'],TestData['RejectionComments'])
        objCreateScar.ValidateRCCARejection_ECD()
        objLogin.QET_LogOut()


    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency(depends=["Test_SCAR::test_TC006_SCAR_ApproveContainmentPhase"])
    def test_TC013_SCAR_RCCAPhase_RejectRCCA(self, setup, TestData):
        strData = self.test_TC006_SCAR_ApproveContainmentPhase(setup, TestData)
        # Login back to Supplier to create RCCA
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['Supplier_UserName'], TestData['Supplier_Password'])
        objSupplier.Supplier_AddRCCA(strData['ScarID'], TestData['CA_Title'], TestData['CA_Description'])
        objLogin.QET_LogOut()
        objCommon.CloseBrowser()

        # Login with User to Approve
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['UserName'], TestData['Password'])
        objCreateScar.User_RCCA_RejectRCCA(strData['ScarID'],TestData['RejectionComments'])
        objLogin.QET_LogOut()



    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    # @pytest.mark.dependency(depends=["Test_SCAR::test_TC010_SCAR_ApproveRCCAPhase"])
    def test_TC014_SCAR_ValidationPhase_EditAction(self, setup, TestData):
        strData = self.test_TC010_SCAR_ApproveRCCAPhase(setup, TestData)
        # Login with Supplier to Add Deliverables
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['Supplier_UserName'], TestData['Supplier_Password'])
        objSupplier.Supplier_EditDeliverables(strData['ScarID'],TestData['CA_Title'],TestData['CA_Description'], TestData['CA_UpdatedTitle'])
        objLogin.QET_LogOut()


    @pytest.mark.regression
    @pytest.mark.P2
    @pytest.mark.dependency()
    # @pytest.mark.dependency(depends=["Test_SCAR::test_TC010_SCAR_ApproveRCCAPhase"])
    def test_TC015_SCAR_ValidationPhase_DeleteAction(self, setup, TestData):
        strData = self.test_TC010_SCAR_ApproveRCCAPhase(setup, TestData)
        # Login with Supplier to Add Deliverables
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['Supplier_UserName'], TestData['Supplier_Password'])
        objSupplier.Supplier_Validation_DeleteAction(strData['ScarID'], TestData['CA_Title'], TestData['CA_Description'])
        objLogin.QET_LogOut()


    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    @pytest.mark.dependency(depends=["Test_SCAR::test_TC010_SCAR_ApproveRCCAPhase"])
    def test_TC016_SCAR_ApproveValidationPhase(self, setup, TestData):
        strData = self.test_TC010_SCAR_ApproveRCCAPhase(setup, TestData)
        # Login with Supplier to Add Deliverables
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['Supplier_UserName'], TestData['Supplier_Password'])
        objSupplier.Supplier_AddDeliverables(strData['ScarID'],TestData['CA_Title'],TestData['CA_Description'])
        objLogin.QET_LogOut()
        objCommon.CloseBrowser()

        #Login with Juniper to Approve
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['UserName'], TestData['Password'])
        objCreateScar.User_ApproveScar(strData['ScarID'])
        objLogin.QET_LogOut()



    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    @pytest.mark.dependency(depends=["Test_SCAR::test_TC010_SCAR_ApproveRCCAPhase"])
    def test_TC017_SCAR_ValidationPhase_RequestForExtension(self, setup, TestData):
        strData = self.test_TC010_SCAR_ApproveRCCAPhase(setup, TestData)
        # Login with Supplier to Add Deliverables
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['Supplier_UserName'], TestData['Supplier_Password'])
        objSupplier.Supplier_AddDeliverables_RequestExtension(strData['ScarID'], TestData['CA_Title'], TestData['CA_Description'])
        objSupplier.SupplierRequestExtension(TestData['ExtensionDays'], TestData['ExtensionReason'])
        objLogin.QET_LogOut()

        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['UserName'], TestData['Password'])
        objCreateScar.User_ApproveScar(strData['ScarID'])
        objLogin.QET_LogOut()



    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    @pytest.mark.dependency(depends=["Test_SCAR::test_TC010_SCAR_ApproveRCCAPhase"])
    def test_TC018_SCAR_ValidationPhase_Reject_RequestForExtension(self, setup, TestData):
        strData = self.test_TC010_SCAR_ApproveRCCAPhase(setup, TestData)
        # Login with Supplier to Add Deliverables
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['Supplier_UserName'], TestData['Supplier_Password'])
        objSupplier.Supplier_AddDeliverables_RequestExtension(strData['ScarID'], TestData['CA_Title'],
                                                                TestData['CA_Description'])
        objSupplier.SupplierRequestExtension(TestData['ExtensionDays'], TestData['ExtensionReason'])
        objLogin.QET_LogOut()

        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['UserName'], TestData['Password'])
        objCreateScar.User_RejectValidation(strData['ScarID'],TestData['RejectionComments'])
        objLogin.QET_LogOut()




    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    @pytest.mark.dependency(depends=["Test_SCAR::test_TC010_SCAR_ApproveRCCAPhase"])
    def test_TC019_SCAR_ValidationPhase_Reject(self, setup, TestData):
        strData = self.test_TC010_SCAR_ApproveRCCAPhase(setup, TestData)
        # Login with Supplier to Add Deliverables
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['Supplier_UserName'], TestData['Supplier_Password'])
        objSupplier.Supplier_AddDeliverables(strData['ScarID'], TestData['CA_Title'], TestData['CA_Description'])
        objLogin.QET_LogOut()
        objCommon.CloseBrowser()

        # Login with Juniper to Approve
        objCommon.LaunchBrowser(strData['URL'])
        objLogin.QET_Login(TestData['UserName'], TestData['Password'])
        objCreateScar.User_RejectValidation(strData['ScarID'],TestData['RejectionComments'])
        objLogin.QET_LogOut()












    #
    # @pytest.mark.dependency()
    # @pytest.mark.regression
    # @pytest.mark.P1
    # def test_TC001_SCAR_CreatingSCAR(self,setup,TestData):
    #     #Creating and Issuing a SCAR
    #     objLogin.QET_Login(TestData['UserName'],TestData['Password'])
    #     strData=objCreateScar.CreateSCAR(TestData['ProblemDescription'],TestData['AffectedPart'],TestData['UserGroup'],TestData['Supplier']
    #                           ,TestData['Contact'],TestData['Escalation'],TestData['Jn_Escalation'],TestData['JnWatchlist'])
    #     logging.info("SCAR Created successfully")
    #     objLogin.QET_LogOut()
    #     objCommon.CloseBrowser()
    #     #Adding Containment using Supplier Login Credentials
    #     objCommon.LaunchBrowser(strData['URL'])
    #     objLogin.QET_Login(TestData['Supplier_UserName'],TestData['Supplier_Password'])
    #     objCreateScar.Supplier_AddingContainment(strData['ScarID'],TestData['CA_Title'],TestData['CA_Description'])
    #     objLogin.QET_LogOut()
    #     objCommon.CloseBrowser()
    #     #Login with User credentials to approve the SCAR
    #     objCommon.LaunchBrowser(strData['URL'])
    #     objLogin.QET_Login(TestData['UserName'],TestData['Password'])
    #     objCreateScar.User_ApproveSCAR(strData['ScarID'])
    #     objLogin.QET_LogOut()
    #     objCommon.CloseBrowser()
    #     # Login back to Supplier to create RCCA
    #     objCommon.LaunchBrowser(strData['URL'])
    #     objLogin.QET_Login(TestData['Supplier_UserName'], TestData['Supplier_Password'])
    #     objCreateScar.Supplier_AddRCCA(strData['ScarID'],TestData['CA_Title'],TestData['CA_Description'])
    #     objLogin.QET_LogOut()
    #     objCommon.CloseBrowser()
    #
    #     #Login with User to Approve
    #     objCommon.LaunchBrowser(strData['URL'])
    #     objLogin.QET_Login(TestData['UserName'], TestData['Password'])
    #     objCreateScar.User_AssignValidationToSupplier(strData['ScarID'])
    #     objLogin.QET_LogOut()
    #     objCommon.CloseBrowser()
    #
    #     #Login with Supplier to Add Deliverables
    #     objCommon.LaunchBrowser(strData['URL'])
    #     objLogin.QET_Login(TestData['Supplier_UserName'], TestData['Supplier_Password'])
    #     objCreateScar.Supplier_AddDeliverables(strData['ScarID'],TestData['CA_Title'],TestData['CA_Description'])
    #     objLogin.QET_LogOut()
    #     objCommon.CloseBrowser()
    #
    #     #Login with Juniper to Approve
    #     objCommon.LaunchBrowser(strData['URL'])
    #     objLogin.QET_Login(TestData['UserName'], TestData['Password'])
    #     objCreateScar.User_ApproveScar(strData['ScarID'])
    #     objLogin.QET_LogOut()











    # @pytest.mark.P1
    # @pytest.mark.sanity
    # @pytest.mark.dependency(depends=["Test_SCAR::test_TC001_SCAR_CreatingSCAR"])
    # def test_TC002_SCAR_CreateAction(self,setup,TestData):
    #     # Test_SCAR.test_TC001_SCAR_CreatingSCAR(self,setup,TestData)
    #     print("test 2 executed")




