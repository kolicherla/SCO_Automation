from QA.BusinessLogic.CreateQI_Page import createQI_Page
from QA.BusinessLogic.Login_Page import login_Page
import pytest

class Test_QI():
    global objLogin, objCreate, objCommon
    objLogin=login_Page()
    objCreate=createQI_Page()

    @pytest.mark.sanity
    @pytest.mark.P1
    # @pytest.mark.dependency()
    def test_TC001_QI_CreatingQI(self,setup,TestData):
        objLogin.QET_Login(TestData['UserName'],TestData['Password'])
        strData=objCreate.CreateQI(TestData['Title'],TestData['ProblemDescription'],TestData['UserGroup'],TestData['DisruptionType']
                          ,TestData['RootcauseOwner'],TestData['RootcauseType'],TestData['EvidenceofDefect'],TestData['HowDetected']
                          ,TestData['impactedCustomer'],TestData['tags'],TestData['AffectedMfgSiteCode'],TestData['Priority'])
        return strData


    @pytest.mark.sanity
    @pytest.mark.P1
    def test_TC002_QI_EditingQI(self, setup, TestData):
        self.test_TC001_QI_CreatingQI(setup, TestData)
        objCreate.EditQI(TestData['DisruptionTypeCurrent'], TestData['RootcauseOwnerCurrent'],
                         TestData['RootcauseTypeCurrent'], TestData['QITeam'], TestData['JNPRAssembly'],
                         TestData['JNPRComponents'], TestData['FieldSeverityLevel'], TestData['FieldCostImpact'],
                         TestData['ImpactDescription'], TestData['Reference'], TestData['ManufacturingSeverityLevel'],
                         TestData['ManufacturingCostImpact'], TestData['JnprImpactDescription'],
                         TestData['ManufacturingReferences'])

    #Containment Phase
    @pytest.mark.sanity
    @pytest.mark.P1
    def test_TC003_QI_Containmentphase(self, setup, TestData):
        self.test_TC002_QI_EditingQI(setup, TestData)
        objCreate.Begin_Cpahse_button('Containment started')
        objCreate.Purge_Action(TestData['PurgeAddAction'], TestData['PurgeProduct'], TestData['strActionTitle'])
        objCreate.Manual_Action(TestData['ManualAddAction'], TestData['strActionTitle'], TestData['strActionDesc'],'Delete')
        objCreate.Manual_Action(TestData['ManualAddAction'], TestData['strActionTitle'], TestData['strActionDesc'],'Markascomplete')
        objCreate.StopShip_Action(TestData['StopShipAction'], TestData['strActionTitle'])


    # RCCA Phase Root Cause Analysis Actions
    @pytest.mark.sanity
    @pytest.mark.P1
    def test_TC004_QI_RootCauseAnalysis(self, setup, TestData):
        self.test_TC003_QI_Containmentphase(setup, TestData)
        objCreate.Resolutionpath_SimpleRCCA_Radio_selection()
        objCreate.RootCause_Add_5why_Action(TestData['FiveWHYAction'], TestData['RootcasueTitle'], TestData['ProblemStatement'], TestData['Why1']
                                            , TestData['Why2'], TestData['Why3'], TestData['Why4'], TestData['Why5'])
        objCreate.Manual_Action(TestData['ManualAddAction'], TestData['strActionTitle'], TestData['strActionDesc'], 'Delete')
        objCreate.Manual_Action(TestData['ManualAddAction'], TestData['strActionTitle'], TestData['strActionDesc'], 'Markascomplete')
        objCreate.RootCause_Fishbone_Action(TestData['FishboneAnalysis'], TestData['RootcasueTitle'],TestData['FishProblemStatement'], TestData['FishConclusion'],
                                            TestData['Categoryone'],TestData['Causeone'],TestData['SecondCategory'],TestData['SecondCause'])

    # RCCA Phase Corrective Actions
    @pytest.mark.sanity
    @pytest.mark.P1
    def test_TC005_QI_CorrectiveActions(self, setup, TestData):
        self.test_TC004_QI_RootCauseAnalysis(setup, TestData)
        objCreate.Manual_Corrective_Action(TestData['ManualAddAction'], TestData['strActionTitle'], TestData['strActionDesc'], 'Markascomplete')
        objCreate.Corrective_SCAR_Action(TestData['SCARAction'], TestData['SCARSupplier'], TestData['Jn_Escalation'],
                                         TestData['Contact'], TestData['Escalation'], TestData['strActionTitle'])
        objCreate.StopShip_Corrective_Action(TestData['StopShipAction'], TestData['strActionTitle'])
        objCreate.PR_Action(TestData['PRAddAction'], TestData['PRProduct'], TestData['strActionTitle'])
        objCreate.Purge_Corrective_Action(TestData['PurgeAddAction'], TestData['PurgeProduct'], TestData['strActionTitle'])


    # RCCA Phase Preventive Actions
    @pytest.mark.sanity
    @pytest.mark.P1
    def test_TC006_QI_PreventiveActions(self, setup, TestData):
        self.test_TC005_QI_CorrectiveActions(setup,TestData)
        objCreate.Preventive_Action(TestData['strActionTitle'], TestData['strActionDesc'], 'Delete')
        objCreate.Preventive_Action(TestData['strActionTitle'], TestData['strActionDesc'], 'Markascomplete')

    # Start a Simple RCCA
    @pytest.mark.sanity
    @pytest.mark.P1
    def test_TC007_QI_SimpleRCCA(self, setup, TestData):
        self.test_TC006_QI_PreventiveActions(setup, TestData)
        objCreate.Complete_QI(TestData['ReasonforClosingQI'])
        objLogin.QET_LogOut()

    # # Start a Simple RCCA Selection
    # @pytest.mark.sanity
    # @pytest.mark.P1
    # def test_TC008_QI_SimpleRCCASelection(self, setup, TestData):
    #     objCreate.Resolutionpath_SimpleRCCA_Radio_selection()


    @pytest.mark.sanity
    @pytest.mark.P1
    def test_TC008_QI_Formal_8D_RootCauseActions(self, setup, TestData):
        self.test_TC003_QI_Containmentphase(setup, TestData)
        objCreate.Resolutionpath_Formal8D_Radio_selection(TestData['QITeam'])
        objCreate.RootCause_Add_5why_Action(TestData['FiveWHYAction'], TestData['RootcasueTitle'],
                                            TestData['ProblemStatement'], TestData['Why1']
                                            , TestData['Why2'], TestData['Why3'], TestData['Why4'], TestData['Why5'])
        objCreate.RootCause_Fishbone_Action(TestData['FishboneAnalysis'], TestData['RootcasueTitle'],
                                            TestData['FishProblemStatement'], TestData['FishConclusion'],
                                            TestData['Categoryone'], TestData['Causeone'], TestData['SecondCategory'],
                                            TestData['SecondCause'])
        objCreate.Manual_Action(TestData['ManualAddAction'], TestData['strActionTitle'], TestData['strActionDesc'], 'Delete')
        objCreate.Manual_Action(TestData['ManualAddAction'], TestData['strActionTitle'], TestData['strActionDesc'], 'Markascomplete')

    @pytest.mark.sanity
    @pytest.mark.P1
    def test_TC009_QI_Formal_8D_CorrectiveActions(self, setup, TestData):
        self.test_TC008_QI_Formal_8D_RootCauseActions(setup, TestData)
        objCreate.Manual_Corrective_Action(TestData['ManualAddAction'], TestData['strActionTitle'], TestData['strActionDesc'], 'Markascomplete')
        objCreate.Corrective_SCAR_Action(TestData['SCARAction'], TestData['SCARSupplier'], TestData['Jn_Escalation'],
                                         TestData['Contact'], TestData['Escalation'], TestData['strActionTitle'])
        objCreate.StopShip_Corrective_Action(TestData['StopShipAction'], TestData['strActionTitle'])
        objCreate.PR_Action(TestData['PRAddAction'], TestData['PRProduct'], TestData['strActionTitle'])
        objCreate.Purge_Corrective_Action(TestData['PurgeAddAction'], TestData['PurgeProduct'], TestData['strActionTitle'])

    @pytest.mark.sanity
    @pytest.mark.P1
    def test_TC010_QI_Formal_8D_CompleteAction(self, setup, TestData):
        self.test_TC009_QI_Formal_8D_CorrectiveActions(setup,TestData)
        objCreate.Preventive_Action(TestData['strActionTitle'], TestData['strActionDesc'], 'Markascomplete')
        objCreate.Begin_Cpahse_button('')
        objCreate.Preventive_Action(TestData['strActionTitle'], TestData['strActionDesc'], 'Markascomplete')
        objCreate.Complete_QI(TestData['ReasonforClosingQI'])



    @pytest.mark.sanity
    @pytest.mark.P1
    def test_TC011_QI_Close_QI(self, setup, TestData):
        self.test_TC001_QI_CreatingQI(setup, TestData)
        objCreate.Affected_items_All_Selection()
        objCreate.Begin_Cpahse_button('Containment started')
        objCreate.Purge_Action(TestData['PurgeAddAction'], TestData['PurgeProduct'], TestData['strActionTitle'])
        objCreate.Manual_Action(TestData['ManualAddAction'], TestData['strActionTitle'], TestData['strActionDesc'], 'Delete')
        objCreate.Manual_Action(TestData['ManualAddAction'], TestData['strActionTitle'], TestData['strActionDesc'], 'Markascomplete')
        objCreate.StopShip_Action(TestData['StopShipAction'], TestData['strActionTitle'])
        objCreate.Resolutionpath_CloseQI_Radio_selection(TestData['ReasonforClosingQI'])

    @pytest.mark.sanity
    @pytest.mark.P2
    def test_TC012_QI_Cancel_QI(self, setup, TestData):
        self.test_TC001_QI_CreatingQI(setup, TestData)
        objCreate.Close_QI(TestData['ReasonforClosingQI'])




