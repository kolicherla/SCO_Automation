from QA.BusinessLogic.CreateJPCN_Page import createJPCN_Page
from QA.BusinessLogic.Login_Page import login_Page
from QA.Utilities.CommonLib import CommonFunctions
from QA.BusinessLogic.JPCNStatusOverview_Page import JPCNstatusoverview_Page
from QA.BusinessLogic.SwitchToOtherRoles_Page import SwitchToRoles_Page
from QA.BusinessLogic.InitialAssessment_Page import InitilaAssessment_Page
from QA.BusinessLogic.Home_Page import Home
from QA.BusinessLogic.ClosureAssessment_Page import ClosureAssessment_Page
from QA.BusinessLogic.CompletedAssessment_Page import CompleteAssessment_Page
from QA.BusinessLogic.Search_Page import Search_Page
from QA.BusinessLogic.mySql_Connections import mySql_Connections
from QA.Base.Config import MyConfigFiles
import pytest
import time


class Test_PCN():
    global objLogin, objCreateJPCN, objCommon,objJPCNStatusOverview, objSwitchToRoles, objHome,objInitalAssessment,objClosureAssessment,objCompleteAssessment,objSearch,objMysql
    objLogin=login_Page()
    objCreateJPCN=createJPCN_Page()
    objCommon = CommonFunctions()
    objJPCNStatusOverview=JPCNstatusoverview_Page()
    objSwitchToRoles=SwitchToRoles_Page()
    objHome=Home()
    objInitalAssessment=InitilaAssessment_Page()
    objClosureAssessment=ClosureAssessment_Page()
    objCompleteAssessment=CompleteAssessment_Page()
    objSearch=Search_Page()
    objMysql=mySql_Connections()

    # PCN login and  Switch roles
    @pytest.mark.dependency()
    @pytest.mark.regression
    @pytest.mark.P1
    def test_TC001_PCN_Switchtootherroles(self, setup, TestData):
        objCommon.LoadURL(MyConfigFiles.AppURL)
        # objLogin.PCN_Login(TestData['UserName'], TestData['Password'])
        # objSwitchToRoles.SwitchToRole("Context CE")
        # objLogin.PCN_LogOut()

    #Create JPCN
    @pytest.mark.dependency()
    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency(depends=["Test_PCN::test_TC001_PCN_Switchtootherroles"])
    def test_TC002_PCN_CreateJPCN(self, setup, TestData):
        # self.test_TC001_PCN_Switchtootherroles(setup, TestData)
        objCommon.LoadURL(MyConfigFiles.AppURL)
        objLogin.PCN_Login(TestData['UserName'], TestData['Password'])
        objSwitchToRoles.SwitchToRole("Context CE")
        objCreateJPCN.CreateJPCN(TestData['SupplierName'])
        strDate=objCreateJPCN.PCN_DateSelections(TestData['PCN_EffDays'],TestData['PCNTYPE'],TestData['LT_BuyDays'],TestData['LT_ShipDays'])
        [strJPNID,strgetData1]=objCreateJPCN.PDNinfo_form(TestData['PCNSource'] ,TestData['Natureofchange'],TestData['Typeofchange'])
        objLogin.PCN_LogOut()
        return strJPNID ,strgetData1,strDate

    @pytest.mark.dependency()
    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency(depends=["Test_PCN::test_TC002_PCN_CreateJPCN"])
    def test_TC003_PCN_Horizon_PrePCN_Validations(self, setup, TestData):
        # self.test_TC002_PCN_CreateJPCN(setup, TestData)
        objCommon.LoadURL(MyConfigFiles.AppURL)
        objLogin.PCN_Login(TestData['UserName'], TestData['Password'])
        objSwitchToRoles.SwitchToRole("Context CE")
        objCreateJPCN.CreateJPCN(TestData['SupplierName'])
        strDate = objCreateJPCN.PCN_DateSelections(TestData['PCN_EffDays'], TestData['PCNTYPE'], TestData['LT_BuyDays'],  TestData['LT_ShipDays'])
        [strJPNID, strgetData1] = objCreateJPCN.PDNinfo_form(TestData['PCNSource'], TestData['Natureofchange'], TestData['Typeofchange'])
        objCreateJPCN.Validate_CCE_PrePoulated_Values()
        objCreateJPCN.Validate_InvalidPCN_Status(TestData['PCNStatus_Open'])
        objCreateJPCN.Validate_InvalidPCN_Status(TestData['PCNStatus_Reopen'])
        objCreateJPCN.ClosethisPCN(TestData['PCNStatus_Closed'])
        objLogin.PCN_LogOut()
        return strJPNID, strgetData1, strDate

    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    @pytest.mark.dependency(depends=["Test_PCN::test_TC003_PCN_Horizon_PrePCN_Validations"])
    def test_TC004_PCN_InformationalNotice_Validations(self, setup, TestData):
        # self.test_TC003_PCN_Horizon_PrePCN_Validations(setup,TestData)
        objCommon.LoadURL(MyConfigFiles.AppURL)
        objLogin.PCN_Login(TestData['UserName'], TestData['Password'])
        objSwitchToRoles.SwitchToRole("Context CE")
        objCreateJPCN.CreateJPCN(TestData['SupplierName'])
        strDate = objCreateJPCN.PCN_DateSelections(TestData['PCN_EffDays'], TestData['PCNTYPE'], TestData['LT_BuyDays'], TestData['LT_ShipDays'])
        [strJPNID, strgetData1] = objCreateJPCN.PDNinfo_form(TestData['PCNSource'], TestData['Natureofchange'],  TestData['Typeofchange'])
        objCreateJPCN.Validate_CCE_PrePoulated_Values()
        objCreateJPCN.Validate_InvalidPCN_Status(TestData['PCNStatus_Open'])
        objCreateJPCN.Validate_InvalidPCN_Status(TestData['PCNStatus_Reopen'])
        objCreateJPCN.ClosethisPCN(TestData['PCNStatus_Closed'])
        objLogin.PCN_LogOut()
        return strJPNID, strgetData1, strDate

   #**************************************NO-IMPACT FLOW*************************************************
    @pytest.mark.dependency()
    @pytest.mark.regression
    @pytest.mark.P1
    # @pytest.mark.dependency(depends=["Test_PCN::test_TC002_PCN_CreateJPCN"])
    def test_TC005_PCN_ProcessChange_Validations(self, setup, TestData):
        # [strJPNID,strgetData1,strDate]=self.test_TC002_PCN_CreateJPCN(setup, TestData)
        objCommon.LoadURL(MyConfigFiles.AppURL)
        objLogin.PCN_Login(TestData['UserName'], TestData['Password'])
        objSwitchToRoles.SwitchToRole("Context CE")
        objCreateJPCN.CreateJPCN(TestData['SupplierName'])
        strDate = objCreateJPCN.PCN_DateSelections(TestData['PCN_EffDays'], TestData['PCNTYPE'], TestData['LT_BuyDays'], TestData['LT_ShipDays'])
        [strJPNID, strgetData1] = objCreateJPCN.PDNinfo_form(TestData['PCNSource'], TestData['Natureofchange'], TestData['Typeofchange'])
        objCreateJPCN.JPN_MPN_Info('NoImpactFound1')
        objCreateJPCN.Uploadvalidation()
        objJPCNStatusOverview.ClickContextCE_Create_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.JPN_MPN_Info_ValidationCheck()
        objCreateJPCN.Validate_CCE_PrePoulated_Values()
        objCreateJPCN.Validate_InvalidPCN_Status(TestData['PCNStatus_Open'])
        objCreateJPCN.Validate_InvalidPCN_Status(TestData['PCNStatus_Reopen'])
        objCreateJPCN.ClosethisPCN(TestData['PCNStatus_Closed'])
        objLogin.PCN_LogOut()
        return strJPNID, strgetData1, strDate



    @pytest.mark.dependency()
    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency(depends=["Test_PCN::test_TC005_PCN_ProcessChange_Validations"])
    def test_TC006_PCN_DesignChange_Validations(self, setup, TestData):
        # strJPNID=self.test_TC005_PCN_ProcessChange_Validations(setup,TestData)
        objCommon.LoadURL(MyConfigFiles.AppURL)
        objLogin.PCN_Login(TestData['UserName'], TestData['Password'])
        objSwitchToRoles.SwitchToRole("Context CE")
        objCreateJPCN.CreateJPCN(TestData['SupplierName'])
        strDate = objCreateJPCN.PCN_DateSelections(TestData['PCN_EffDays'], TestData['PCNTYPE'], TestData['LT_BuyDays'], TestData['LT_ShipDays'])
        [strJPNID, strgetData1] = objCreateJPCN.PDNinfo_form(TestData['PCNSource'], TestData['Natureofchange'],  TestData['Typeofchange'])
        objCreateJPCN.JPN_MPN_Info('NoImpactFound1')
        objCreateJPCN.Uploadvalidation()
        objJPCNStatusOverview.ClickContextCE_Create_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.JPN_MPN_Info_ValidationCheck()
        objCreateJPCN.Validate_CCE_PrePoulated_Values()
        objCreateJPCN.Validate_InvalidPCN_Status(TestData['PCNStatus_Open'])
        objCreateJPCN.Validate_InvalidPCN_Status(TestData['PCNStatus_Reopen'])
        objCreateJPCN.ClosethisPCN(TestData['PCNStatus_Closed'])
        objLogin.PCN_LogOut()
        return strJPNID, strgetData1, strDate


    @pytest.mark.dependency()
    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency(depends=["Test_PCN::test_TC005_PCN_ProcessChange_Validations"])
    def test_TC007_PCN_EOL_Validations(self, setup, TestData):
        # strJPNID = self.test_TC005_PCN_ProcessChange_Validations(setup, TestData)
        objCommon.LoadURL(MyConfigFiles.AppURL)
        objLogin.PCN_Login(TestData['UserName'], TestData['Password'])
        objSwitchToRoles.SwitchToRole("Context CE")
        objCreateJPCN.CreateJPCN(TestData['SupplierName'])
        strDate = objCreateJPCN.PCN_DateSelections(TestData['PCN_EffDays'], TestData['PCNTYPE'], TestData['LT_BuyDays'], TestData['LT_ShipDays'])
        [strJPNID, strgetData1] = objCreateJPCN.PDNinfo_form(TestData['PCNSource'], TestData['Natureofchange'],  TestData['Typeofchange'])
        objCreateJPCN.JPN_MPN_Info('NoImpactFound1')
        objCreateJPCN.Uploadvalidation()
        objJPCNStatusOverview.ClickContextCE_Create_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.JPN_MPN_Info_ValidationCheck()
        objCreateJPCN.Validate_CCE_PrePoulated_Values()
        objCreateJPCN.Validate_InvalidPCN_Status(TestData['PCNStatus_Open'])
        objCreateJPCN.Validate_InvalidPCN_Status(TestData['PCNStatus_Reopen'])
        objCreateJPCN.ClosethisPCN(TestData['PCNStatus_Closed'])
        objLogin.PCN_LogOut()
        return strJPNID, strgetData1, strDate
        # return strJPNID


#PCN Flow-Create Stage For Process Change
    @pytest.mark.dependency()
    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency(depends=["Test_PCN::test_TC002_PCN_CreateJPCN"])
    def test_TC008_PCN_CreatePCN_For_PCNTYPE_Process_Change(self, setup, TestData):
        # [strJPNID,strgetData1,strDate] = self.test_TC002_PCN_CreateJPCN(setup, TestData)
        objCommon.LoadURL(MyConfigFiles.AppURL)
        objLogin.PCN_Login(TestData['UserName'], TestData['Password'])
        objSwitchToRoles.SwitchToRole("Context CE")
        objCreateJPCN.CreateJPCN(TestData['SupplierName'])
        strDate = objCreateJPCN.PCN_DateSelections(TestData['PCN_EffDays'], TestData['PCNTYPE'], TestData['LT_BuyDays'], TestData['LT_ShipDays'])
        [strJPNID, strgetData1] = objCreateJPCN.PDNinfo_form(TestData['PCNSource'], TestData['Natureofchange'], TestData['Typeofchange'])
        objCreateJPCN.JPN_MPN_Info('MaximSupplierStatus1')
        objCreateJPCN.Uploadvalidation()
        objJPCNStatusOverview.ClickContextCE_Create_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_BackButton_Navigation()
        objCreateJPCN.Edit_EnterPCNDetails_Page()
        objCreateJPCN.EOL_InvistigationFileUpload_fromJPNTable1('EOL-Investigation-Form')
        objCreateJPCN.EOL_Upload_Validations(TestData['strResponsibleCoreCE'])
        objCreateJPCN.GetCoreCENames()
        objCreateJPCN.GetCommodityGroups()
        objCreateJPCN.readExcelData_Compare_SupplierStatus('SupplierMapping', TestData['SupplierName'])
        objCreateJPCN.AddNewAttachement_JPNMPN(TestData['strCategory'], 'MPN4', 'enter')
        objCreateJPCN.DeleteAttachement()
        objCreateJPCN.PreviewScreen_Validations()
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section()
        objCreateJPCN.WhereUserAnalysis(TestData['PCNTYPE'], TestData['strCategory'], 'MPN4', 'enter')
        objLogin.PCN_LogOut()
        return strJPNID ,strgetData1,strDate

 #PCN Flow-Create Stage For Design Changee**
    @pytest.mark.dependency()
    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency(depends=["Test_PCN::test_TC008_PCN_CreatePCN_For_PCNTYPE_Process_Change"])
    def test_TC009_PCN_CreatePCN_For_PCNTYPE_Design_Change(self, setup, TestData):
        # [strJPNID, strgetData1,strDate] = self.test_TC008_PCN_CreatePCN_For_PCNTYPE_Process_Change(setup, TestData)
        objCommon.LoadURL(MyConfigFiles.AppURL)
        objLogin.PCN_Login(TestData['UserName'], TestData['Password'])
        objSwitchToRoles.SwitchToRole("Context CE")
        objCreateJPCN.CreateJPCN(TestData['SupplierName'])
        strDate = objCreateJPCN.PCN_DateSelections(TestData['PCN_EffDays'], TestData['PCNTYPE'], TestData['LT_BuyDays'], TestData['LT_ShipDays'])
        [strJPNID, strgetData1] = objCreateJPCN.PDNinfo_form(TestData['PCNSource'], TestData['Natureofchange'],  TestData['Typeofchange'])
        objCreateJPCN.JPN_MPN_Info('MaximSupplierStatus1')
        objCreateJPCN.Uploadvalidation()
        objJPCNStatusOverview.ClickContextCE_Create_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_BackButton_Navigation()
        objCreateJPCN.Edit_EnterPCNDetails_Page()
        objCreateJPCN.EOL_InvistigationFileUpload_fromJPNTable1('EOL-Investigation-Form')
        objCreateJPCN.EOL_Upload_Validations(TestData['strResponsibleCoreCE'])
        objCreateJPCN.GetCoreCENames()
        objCreateJPCN.GetCommodityGroups()
        objCreateJPCN.readExcelData_Compare_SupplierStatus('SupplierMapping', TestData['SupplierName'])
        objCreateJPCN.AddNewAttachement_JPNMPN(TestData['strCategory'], 'MPN4', 'enter')
        objCreateJPCN.DeleteAttachement()
        objCreateJPCN.PreviewScreen_Validations()
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section()
        objCreateJPCN.WhereUserAnalysis(TestData['PCNTYPE'], TestData['strCategory'], 'MPN4', 'enter')
        objLogin.PCN_LogOut()
        return strJPNID, strgetData1, strDate
        # return strJPNID ,strgetData1,strDate

#PDN Flow-Create Stage For EOL
    @pytest.mark.dependency()
    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency(depends=["Test_PCN::test_TC008_PCN_CreatePCN_For_PCNTYPE_Process_Change"])
    def test_TC010_PCN_CreatePDN_For_PCNTYPE_EOL(self, setup, TestData):
        # [strJPNID, strgetData1,strDate] = self.test_TC008_PCN_CreatePCN_For_PCNTYPE_Process_Change(setup, TestData)
        objCommon.LoadURL(MyConfigFiles.AppURL)
        objLogin.PCN_Login(TestData['UserName'], TestData['Password'])
        objSwitchToRoles.SwitchToRole("Context CE")
        objCreateJPCN.CreateJPCN(TestData['SupplierName'])
        strDate = objCreateJPCN.PCN_DateSelections(TestData['PCN_EffDays'], TestData['PCNTYPE'], TestData['LT_BuyDays'], TestData['LT_ShipDays'])
        [strJPNID, strgetData1] = objCreateJPCN.PDNinfo_form(TestData['PCNSource'], TestData['Natureofchange'], TestData['Typeofchange'])
        objCreateJPCN.JPN_MPN_Info('MaximSupplierStatus1')
        objCreateJPCN.Uploadvalidation()
        objJPCNStatusOverview.ClickContextCE_Create_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_BackButton_Navigation()
        objCreateJPCN.Edit_EnterPCNDetails_Page()
        objCreateJPCN.EOL_InvistigationFileUpload_fromJPNTable1('EOL-Investigation-Form')
        objCreateJPCN.EOL_Upload_Validations(TestData['strResponsibleCoreCE'])
        objCreateJPCN.GetCoreCENames()
        objCreateJPCN.GetCommodityGroups()
        objCreateJPCN.readExcelData_Compare_SupplierStatus('SupplierMapping', TestData['SupplierName'])
        objCreateJPCN.AddNewAttachement_JPNMPN(TestData['strCategory'], 'MPN4', 'enter')
        objCreateJPCN.DeleteAttachement()
        objCreateJPCN.PreviewScreen_Validations()
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section()
        objCreateJPCN.WhereUserAnalysis(TestData['PCNTYPE'], TestData['strCategory'], 'MPN4', 'enter')
        objLogin.PCN_LogOut()
        return strJPNID, strgetData1, strDate

        # return strJPNID,strgetData1,strDate

 # ***************************************PCN Initial Assessment Workflow-Create Stage*************************************************
    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    @pytest.mark.dependency(depends=["Test_PCN::test_TC008_PCN_CreatePCN_For_PCNTYPE_Process_Change"])
    def test_TC011_PCN_InitialAssessment_For_ProcessChangePCNType_Verify_Morethan90days(self, setup, TestData):
        # [strJPNID,strgetData1,strDate] = self.test_TC008_PCN_CreatePCN_For_PCNTYPE_Process_Change(setup, TestData)
        objCommon.LoadURL(MyConfigFiles.AppURL)
        objLogin.PCN_Login(TestData['UserName'], TestData['Password'])
        objSwitchToRoles.SwitchToRole("Context CE")
        objCreateJPCN.CreateJPCN(TestData['SupplierName'])
        strDate = objCreateJPCN.PCN_DateSelections(TestData['PCN_EffDays'], TestData['PCNTYPE'], TestData['LT_BuyDays'], TestData['LT_ShipDays'])
        [strJPNID, strgetData1] = objCreateJPCN.PDNinfo_form(TestData['PCNSource'], TestData['Natureofchange'],  TestData['Typeofchange'])
        objCreateJPCN.JPN_MPN_Info('MaximSupplierStatus1')
        objCreateJPCN.Uploadvalidation()
        objJPCNStatusOverview.ClickContextCE_Create_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_BackButton_Navigation()
        objCreateJPCN.Edit_EnterPCNDetails_Page()
        objCreateJPCN.EOL_InvistigationFileUpload_fromJPNTable1('EOL-Investigation-Form')
        objCreateJPCN.EOL_Upload_Validations(TestData['strResponsibleCoreCE'])
        objCreateJPCN.GetCoreCENames()
        objCreateJPCN.GetCommodityGroups()
        objCreateJPCN.readExcelData_Compare_SupplierStatus('SupplierMapping', TestData['SupplierName'])
        objCreateJPCN.AddNewAttachement_JPNMPN(TestData['strCategory'], 'MPN4', 'enter')
        objCreateJPCN.DeleteAttachement()
        objCreateJPCN.PreviewScreen_Validations()
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section()
        objCreateJPCN.WhereUserAnalysis(TestData['PCNTYPE'], TestData['strCategory'], 'MPN4', 'enter')
        objJPCNStatusOverview.ClickContextCE_InitialAssessment_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section()
        objInitalAssessment.InitialAssessment_ContextCE_Details(TestData['CCER'], TestData['priorityType'],TestData['PCNTYPE'],TestData['ASQNeeded'])
        objInitalAssessment.InitialAssessment_AddNewRecord(TestData['DeviationStatus'],TestData['MCOECO'])
        objInitalAssessment.QualDataReview_Attachement('QualReport',TestData['QualReportStatus'])
        objInitalAssessment.InitialAssessment_Checking_AutoPopulationOfPCNCompliance(TestData['PCNTYPE'],strDate['EFRCDiff'], strDate['BRDiff'],strDate['SBDiff'] ,TestData['ReasonforNC'])
        objInitalAssessment.Complete_Assessment()
        objLogin.PCN_LogOut()
        return strJPNID,strgetData1,strDate

    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    @pytest.mark.dependency(depends=["Test_PCN::test_TC011_PCN_InitialAssessment_For_ProcessChangePCNType_Verify_Morethan90days"])
    def test_TC012_PCN_InitialAssessment_For_DesignChangePCNType_Verify_Morethan90days(self, setup, TestData):
        # self.test_TC011_PCN_InitialAssessment_For_ProcessChangePCNType_Verify_Morethan90days(setup, TestData)
        objCommon.LoadURL(MyConfigFiles.AppURL)
        objLogin.PCN_Login(TestData['UserName'], TestData['Password'])
        objSwitchToRoles.SwitchToRole("Context CE")
        objCreateJPCN.CreateJPCN(TestData['SupplierName'])
        strDate = objCreateJPCN.PCN_DateSelections(TestData['PCN_EffDays'], TestData['PCNTYPE'], TestData['LT_BuyDays'], TestData['LT_ShipDays'])
        [strJPNID, strgetData1] = objCreateJPCN.PDNinfo_form(TestData['PCNSource'], TestData['Natureofchange'], TestData['Typeofchange'])
        objCreateJPCN.JPN_MPN_Info('MaximSupplierStatus1')
        objCreateJPCN.Uploadvalidation()
        objJPCNStatusOverview.ClickContextCE_Create_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_BackButton_Navigation()
        objCreateJPCN.Edit_EnterPCNDetails_Page()
        objCreateJPCN.EOL_InvistigationFileUpload_fromJPNTable1('EOL-Investigation-Form')
        objCreateJPCN.EOL_Upload_Validations(TestData['strResponsibleCoreCE'])
        objCreateJPCN.GetCoreCENames()
        objCreateJPCN.GetCommodityGroups()
        objCreateJPCN.readExcelData_Compare_SupplierStatus('SupplierMapping', TestData['SupplierName'])
        objCreateJPCN.AddNewAttachement_JPNMPN(TestData['strCategory'], 'MPN4', 'enter')
        objCreateJPCN.DeleteAttachement()
        objCreateJPCN.PreviewScreen_Validations()
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section()
        objCreateJPCN.WhereUserAnalysis(TestData['PCNTYPE'], TestData['strCategory'], 'MPN4', 'enter')
        objJPCNStatusOverview.ClickContextCE_InitialAssessment_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section()
        objInitalAssessment.InitialAssessment_ContextCE_Details(TestData['CCER'], TestData['priorityType'], TestData['PCNTYPE'], TestData['ASQNeeded'])
        objInitalAssessment.InitialAssessment_AddNewRecord(TestData['DeviationStatus'], TestData['MCOECO'])
        objInitalAssessment.QualDataReview_Attachement('QualReport', TestData['QualReportStatus'])
        objInitalAssessment.InitialAssessment_Checking_AutoPopulationOfPCNCompliance(TestData['PCNTYPE'],strDate['EFRCDiff'], strDate['BRDiff'], strDate['SBDiff'], TestData['ReasonforNC'])
        objInitalAssessment.Complete_Assessment()
        objLogin.PCN_LogOut()
        return strJPNID, strgetData1, strDate

    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    @pytest.mark.dependency(depends=["Test_PCN::test_TC011_PCN_InitialAssessment_For_ProcessChangePCNType_Verify_Morethan90days"])
    def test_TC013_PCN_InitialAssessment_For_DesignChangePCNType_Verify_lessthan90days(self, setup, TestData):
        # self.test_TC011_PCN_InitialAssessment_For_ProcessChangePCNType_Verify_Morethan90days(setup, TestData)
        objCommon.LoadURL(MyConfigFiles.AppURL)
        objLogin.PCN_Login(TestData['UserName'], TestData['Password'])
        objSwitchToRoles.SwitchToRole("Context CE")
        objCreateJPCN.CreateJPCN(TestData['SupplierName'])
        strDate = objCreateJPCN.PCN_DateSelections(TestData['PCN_EffDays'], TestData['PCNTYPE'], TestData['LT_BuyDays'], TestData['LT_ShipDays'])
        [strJPNID, strgetData1] = objCreateJPCN.PDNinfo_form(TestData['PCNSource'], TestData['Natureofchange'],  TestData['Typeofchange'])
        objCreateJPCN.JPN_MPN_Info('MaximSupplierStatus1')
        objCreateJPCN.Uploadvalidation()
        objJPCNStatusOverview.ClickContextCE_Create_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_BackButton_Navigation()
        objCreateJPCN.Edit_EnterPCNDetails_Page()
        objCreateJPCN.EOL_InvistigationFileUpload_fromJPNTable1('EOL-Investigation-Form')
        objCreateJPCN.EOL_Upload_Validations(TestData['strResponsibleCoreCE'])
        objCreateJPCN.GetCoreCENames()
        objCreateJPCN.GetCommodityGroups()
        objCreateJPCN.readExcelData_Compare_SupplierStatus('SupplierMapping', TestData['SupplierName'])
        objCreateJPCN.AddNewAttachement_JPNMPN(TestData['strCategory'], 'MPN4', 'enter')
        objCreateJPCN.DeleteAttachement()
        objCreateJPCN.PreviewScreen_Validations()
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section()
        objCreateJPCN.WhereUserAnalysis(TestData['PCNTYPE'], TestData['strCategory'], 'MPN4', 'enter')
        objJPCNStatusOverview.ClickContextCE_InitialAssessment_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section()
        objInitalAssessment.InitialAssessment_ContextCE_Details(TestData['CCER'], TestData['priorityType'], TestData['PCNTYPE'], TestData['ASQNeeded'])
        objInitalAssessment.InitialAssessment_AddNewRecord(TestData['DeviationStatus'], TestData['MCOECO'])
        objInitalAssessment.QualDataReview_Attachement('QualReport', TestData['QualReportStatus'])
        objInitalAssessment.InitialAssessment_Checking_AutoPopulationOfPCNCompliance(TestData['PCNTYPE'], strDate['EFRCDiff'], strDate['BRDiff'], strDate['SBDiff'],
                                                                                     TestData['ReasonforNC'])
        objInitalAssessment.Complete_Assessment()
        objLogin.PCN_LogOut()
        return strJPNID, strgetData1, strDate

    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    @pytest.mark.dependency(depends=["Test_PCN::test_TC011_PCN_InitialAssessment_For_ProcessChangePCNType_Verify_Morethan90days"])
    def test_TC014_PCN_InitialAssessment_For_ProcessChangePCNType_Verify_lessthan90days(self, setup, TestData):
        # self.test_TC011_PCN_InitialAssessment_For_ProcessChangePCNType_Verify_Morethan90days(setup, TestData)
        objCommon.LoadURL(MyConfigFiles.AppURL)
        objLogin.PCN_Login(TestData['UserName'], TestData['Password'])
        objSwitchToRoles.SwitchToRole("Context CE")
        objCreateJPCN.CreateJPCN(TestData['SupplierName'])
        strDate = objCreateJPCN.PCN_DateSelections(TestData['PCN_EffDays'], TestData['PCNTYPE'], TestData['LT_BuyDays'], TestData['LT_ShipDays'])
        [strJPNID, strgetData1] = objCreateJPCN.PDNinfo_form(TestData['PCNSource'], TestData['Natureofchange'], TestData['Typeofchange'])
        objCreateJPCN.JPN_MPN_Info('MaximSupplierStatus1')
        objCreateJPCN.Uploadvalidation()
        objJPCNStatusOverview.ClickContextCE_Create_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_BackButton_Navigation()
        objCreateJPCN.Edit_EnterPCNDetails_Page()
        objCreateJPCN.EOL_InvistigationFileUpload_fromJPNTable1('EOL-Investigation-Form')
        objCreateJPCN.EOL_Upload_Validations(TestData['strResponsibleCoreCE'])
        objCreateJPCN.GetCoreCENames()
        objCreateJPCN.GetCommodityGroups()
        objCreateJPCN.readExcelData_Compare_SupplierStatus('SupplierMapping', TestData['SupplierName'])
        objCreateJPCN.AddNewAttachement_JPNMPN(TestData['strCategory'], 'MPN4', 'enter')
        objCreateJPCN.DeleteAttachement()
        objCreateJPCN.PreviewScreen_Validations()
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section()
        objCreateJPCN.WhereUserAnalysis(TestData['PCNTYPE'], TestData['strCategory'], 'MPN4', 'enter')
        objJPCNStatusOverview.ClickContextCE_InitialAssessment_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section()
        objInitalAssessment.InitialAssessment_ContextCE_Details(TestData['CCER'], TestData['priorityType'], TestData['PCNTYPE'], TestData['ASQNeeded'])
        objInitalAssessment.InitialAssessment_AddNewRecord(TestData['DeviationStatus'], TestData['MCOECO'])
        objInitalAssessment.QualDataReview_Attachement('QualReport', TestData['QualReportStatus'])
        objInitalAssessment.InitialAssessment_Checking_AutoPopulationOfPCNCompliance(TestData['PCNTYPE'], strDate['EFRCDiff'], strDate['BRDiff'], strDate['SBDiff'],
                                                                                     TestData['ReasonforNC'])
        objInitalAssessment.Complete_Assessment()
        objLogin.PCN_LogOut()
        return strJPNID, strgetData1, strDate

# PDN work flow with Combinations of (Last Time Buy Date) - (PCN Received Date) and (Last Time Ship Date) - (Last Time Buy Date) >= 180
    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    @pytest.mark.dependency(depends=["Test_PCN::test_TC011_PCN_InitialAssessment_For_ProcessChangePCNType_Verify_Morethan90days"])
    def test_TC015_PCN_PDN_InitialAssessment_For_EOLPCNType_Verify_Morethan180days(self, setup, TestData):
        # self.test_TC011_PCN_InitialAssessment_For_ProcessChangePCNType_Verify_Morethan90days(setup, TestData)
        objCommon.LoadURL(MyConfigFiles.AppURL)
        objLogin.PCN_Login(TestData['UserName'], TestData['Password'])
        objSwitchToRoles.SwitchToRole("Context CE")
        objCreateJPCN.CreateJPCN(TestData['SupplierName'])
        strDate = objCreateJPCN.PCN_DateSelections(TestData['PCN_EffDays'], TestData['PCNTYPE'], TestData['LT_BuyDays'], TestData['LT_ShipDays'])
        [strJPNID, strgetData1] = objCreateJPCN.PDNinfo_form(TestData['PCNSource'], TestData['Natureofchange'], TestData['Typeofchange'])
        objCreateJPCN.JPN_MPN_Info('MaximSupplierStatus1')
        objCreateJPCN.Uploadvalidation()
        objJPCNStatusOverview.ClickContextCE_Create_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_BackButton_Navigation()
        objCreateJPCN.Edit_EnterPCNDetails_Page()
        objCreateJPCN.EOL_InvistigationFileUpload_fromJPNTable1('EOL-Investigation-Form')
        objCreateJPCN.EOL_Upload_Validations(TestData['strResponsibleCoreCE'])
        objCreateJPCN.GetCoreCENames()
        objCreateJPCN.GetCommodityGroups()
        objCreateJPCN.readExcelData_Compare_SupplierStatus('SupplierMapping', TestData['SupplierName'])
        objCreateJPCN.AddNewAttachement_JPNMPN(TestData['strCategory'], 'MPN4', 'enter')
        objCreateJPCN.DeleteAttachement()
        objCreateJPCN.PreviewScreen_Validations()
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section()
        objCreateJPCN.WhereUserAnalysis(TestData['PCNTYPE'], TestData['strCategory'], 'MPN4', 'enter')
        objJPCNStatusOverview.ClickContextCE_InitialAssessment_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section()
        objInitalAssessment.InitialAssessment_ContextCE_Details(TestData['CCER'], TestData['priorityType'], TestData['PCNTYPE'], TestData['ASQNeeded'])
        objInitalAssessment.InitialAssessment_AddNewRecord(TestData['DeviationStatus'], TestData['MCOECO'])
        objInitalAssessment.QualDataReview_Attachement('QualReport', TestData['QualReportStatus'])
        objInitalAssessment.InitialAssessment_Checking_AutoPopulationOfPCNCompliance(TestData['PCNTYPE'],  strDate['EFRCDiff'], strDate['BRDiff'], strDate['SBDiff'],
                                                                                     TestData['ReasonforNC'])
        objInitalAssessment.Complete_Assessment()
        objLogin.PCN_LogOut()
        return strJPNID, strgetData1, strDate

# PDN work flow with Combinations of (Last Time Buy Date) - (PCN Received Date) and (Last Time Ship Date) - (Last Time Buy Date) < 180
    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    @pytest.mark.dependency(depends=["Test_PCN::test_TC015_PCN_PDN_InitialAssessment_For_EOLPCNType_Verify_Morethan180days"])
    def test_TC016_PCN_PDN_InitialAssessment_For_EOLPCNType_Verify_lessthan180days(self, setup, TestData):
        # self.test_TC015_PCN_PDN_InitialAssessment_For_EOLPCNType_Verify_Morethan180days(setup, TestData)
        objCommon.LoadURL(MyConfigFiles.AppURL)
        objLogin.PCN_Login(TestData['UserName'], TestData['Password'])
        objSwitchToRoles.SwitchToRole("Context CE")
        objCreateJPCN.CreateJPCN(TestData['SupplierName'])
        strDate = objCreateJPCN.PCN_DateSelections(TestData['PCN_EffDays'], TestData['PCNTYPE'], TestData['LT_BuyDays'], TestData['LT_ShipDays'])
        [strJPNID, strgetData1] = objCreateJPCN.PDNinfo_form(TestData['PCNSource'], TestData['Natureofchange'], TestData['Typeofchange'])
        objCreateJPCN.JPN_MPN_Info('MaximSupplierStatus1')
        objCreateJPCN.Uploadvalidation()
        objJPCNStatusOverview.ClickContextCE_Create_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_BackButton_Navigation()
        objCreateJPCN.Edit_EnterPCNDetails_Page()
        objCreateJPCN.EOL_InvistigationFileUpload_fromJPNTable1('EOL-Investigation-Form')
        objCreateJPCN.EOL_Upload_Validations(TestData['strResponsibleCoreCE'])
        objCreateJPCN.GetCoreCENames()
        objCreateJPCN.GetCommodityGroups()
        objCreateJPCN.readExcelData_Compare_SupplierStatus('SupplierMapping', TestData['SupplierName'])
        objCreateJPCN.AddNewAttachement_JPNMPN(TestData['strCategory'], 'MPN4', 'enter')
        objCreateJPCN.DeleteAttachement()
        objCreateJPCN.PreviewScreen_Validations()
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section()
        objCreateJPCN.WhereUserAnalysis(TestData['PCNTYPE'], TestData['strCategory'], 'MPN4', 'enter')
        objJPCNStatusOverview.ClickContextCE_InitialAssessment_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section()
        objInitalAssessment.InitialAssessment_ContextCE_Details(TestData['CCER'], TestData['priorityType'], TestData['PCNTYPE'], TestData['ASQNeeded'])
        objInitalAssessment.InitialAssessment_AddNewRecord(TestData['DeviationStatus'], TestData['MCOECO'])
        objInitalAssessment.QualDataReview_Attachement('QualReport', TestData['QualReportStatus'])
        objInitalAssessment.InitialAssessment_Checking_AutoPopulationOfPCNCompliance(TestData['PCNTYPE'], strDate['EFRCDiff'], strDate['BRDiff'], strDate['SBDiff'],
                                                                                     TestData['ReasonforNC'])
        objInitalAssessment.Complete_Assessment()
        objLogin.PCN_LogOut()
        return strJPNID, strgetData1, strDate

 # PDN work flow with Combinations of (Last Time Buy Date) - (PCN Received Date) and (Last Time Ship Date) - (Last Time Buy Date) < 180
    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    @pytest.mark.dependency(depends=["Test_PCN::test_TC011_PCN_InitialAssessment_For_ProcessChangePCNType_Verify_Morethan90days"])
    def test_TC017_PCN_CoreSE_SendBack_For_ProcessChangePCNType(self, setup, TestData):
        # [strJPNID, strgetData1,strDate]=self.test_TC011_PCN_InitialAssessment_For_ProcessChangePCNType_Verify_Morethan90days(setup, TestData)
        objCommon.LoadURL(MyConfigFiles.AppURL)
        objLogin.PCN_Login(TestData['UserName'], TestData['Password'])
        objSwitchToRoles.SwitchToRole("Context CE")
        objCreateJPCN.CreateJPCN(TestData['SupplierName'])
        strDate = objCreateJPCN.PCN_DateSelections(TestData['PCN_EffDays'], TestData['PCNTYPE'], TestData['LT_BuyDays'], TestData['LT_ShipDays'])
        [strJPNID, strgetData1] = objCreateJPCN.PDNinfo_form(TestData['PCNSource'], TestData['Natureofchange'], TestData['Typeofchange'])
        objCreateJPCN.JPN_MPN_Info('MaximSupplierStatus1')
        objCreateJPCN.Uploadvalidation()
        objJPCNStatusOverview.ClickContextCE_Create_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_BackButton_Navigation()
        objCreateJPCN.Edit_EnterPCNDetails_Page()
        objCreateJPCN.EOL_InvistigationFileUpload_fromJPNTable1('EOL-Investigation-Form')
        objCreateJPCN.EOL_Upload_Validations(TestData['strResponsibleCoreCE'])
        objCreateJPCN.GetCoreCENames()
        objCreateJPCN.GetCommodityGroups()
        objCreateJPCN.readExcelData_Compare_SupplierStatus('SupplierMapping', TestData['SupplierName'])
        objCreateJPCN.AddNewAttachement_JPNMPN(TestData['strCategory'], 'MPN4', 'enter')
        objCreateJPCN.DeleteAttachement()
        objCreateJPCN.PreviewScreen_Validations()
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section()
        objCreateJPCN.WhereUserAnalysis(TestData['PCNTYPE'], TestData['strCategory'], 'MPN4', 'enter')
        objJPCNStatusOverview.ClickContextCE_InitialAssessment_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section()
        objInitalAssessment.InitialAssessment_ContextCE_Details(TestData['CCER'], TestData['priorityType'],  TestData['PCNTYPE'], TestData['ASQNeeded'])
        objInitalAssessment.InitialAssessment_AddNewRecord(TestData['DeviationStatus'], TestData['MCOECO'])
        objInitalAssessment.QualDataReview_Attachement('QualReport', TestData['QualReportStatus'])
        objInitalAssessment.InitialAssessment_Checking_AutoPopulationOfPCNCompliance(TestData['PCNTYPE'], strDate['EFRCDiff'], strDate['BRDiff'], strDate['SBDiff'],
                                                                                     TestData['ReasonforNC'])
        objInitalAssessment.Complete_Assessment()
        objSwitchToRoles.SwitchToRole("Core CE")
        objJPCNStatusOverview.ClickDashboard_Link()
        objJPCNStatusOverview.ClickCoreCE_AssesmnetPending_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objJPCNStatusOverview.SendBack_with_AssignBacktoContextCE(TestData['AssginbackComments'])
        objLogin.PCN_LogOut()
        return strJPNID, strgetData1, strDate


    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    @pytest.mark.dependency(depends=["Test_PCN::test_TC017_PCN_CoreSE_SendBack_For_ProcessChangePCNType"])
    def test_TC018_PCN_Reassign_Assessment(self, setup, TestData):
        # [strJPNID, strgetData1,strDate] = self.test_TC017_PCN_CoreSE_SendBack_For_ProcessChangePCNType(setup, TestData)
        objCommon.LoadURL(MyConfigFiles.AppURL)
        objLogin.PCN_Login(TestData['UserName'], TestData['Password'])
        objSwitchToRoles.SwitchToRole("Context CE")
        objCreateJPCN.CreateJPCN(TestData['SupplierName'])
        strDate = objCreateJPCN.PCN_DateSelections(TestData['PCN_EffDays'], TestData['PCNTYPE'], TestData['LT_BuyDays'], TestData['LT_ShipDays'])
        [strJPNID, strgetData1] = objCreateJPCN.PDNinfo_form(TestData['PCNSource'], TestData['Natureofchange'], TestData['Typeofchange'])
        objCreateJPCN.JPN_MPN_Info('MaximSupplierStatus1')
        objCreateJPCN.Uploadvalidation()
        objJPCNStatusOverview.ClickContextCE_Create_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_BackButton_Navigation()
        objCreateJPCN.Edit_EnterPCNDetails_Page()
        objCreateJPCN.EOL_InvistigationFileUpload_fromJPNTable1('EOL-Investigation-Form')
        objCreateJPCN.EOL_Upload_Validations(TestData['strResponsibleCoreCE'])
        objCreateJPCN.GetCoreCENames()
        objCreateJPCN.GetCommodityGroups()
        objCreateJPCN.readExcelData_Compare_SupplierStatus('SupplierMapping', TestData['SupplierName'])
        objCreateJPCN.AddNewAttachement_JPNMPN(TestData['strCategory'], 'MPN4', 'enter')
        objCreateJPCN.DeleteAttachement()
        objCreateJPCN.PreviewScreen_Validations()
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section()
        objCreateJPCN.WhereUserAnalysis(TestData['PCNTYPE'], TestData['strCategory'], 'MPN4', 'enter')
        objJPCNStatusOverview.ClickContextCE_InitialAssessment_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section()
        objInitalAssessment.InitialAssessment_ContextCE_Details(TestData['CCER'], TestData['priorityType'],  TestData['PCNTYPE'], TestData['ASQNeeded'])
        objInitalAssessment.InitialAssessment_AddNewRecord(TestData['DeviationStatus'], TestData['MCOECO'])
        objInitalAssessment.QualDataReview_Attachement('QualReport', TestData['QualReportStatus'])
        objInitalAssessment.InitialAssessment_Checking_AutoPopulationOfPCNCompliance(TestData['PCNTYPE'], strDate['EFRCDiff'], strDate['BRDiff'], strDate['SBDiff'],
                                                                                     TestData['ReasonforNC'])
        objInitalAssessment.Complete_Assessment()
        objSwitchToRoles.SwitchToRole("Core CE")
        objJPCNStatusOverview.ClickDashboard_Link()
        objJPCNStatusOverview.ClickCoreCE_AssesmnetPending_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objJPCNStatusOverview.SendBack_with_AssignBacktoContextCE(TestData['AssginbackComments'])
        objSwitchToRoles.SwitchToRole("Context CE")
        objJPCNStatusOverview.ClickDashboard_Link()
        objJPCNStatusOverview.Reassign_Assessment()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section()
        objInitalAssessment.InitialAssessment_AddNewRecord(TestData['DeviationStatus'] ,TestData['MCOECO'])
        objInitalAssessment.Complete_Assessment()
        objLogin.PCN_LogOut()
        return strJPNID,strgetData1,strDate

    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    @pytest.mark.dependency(depends=["Test_PCN::test_TC018_PCN_Reassign_Assessment"])
    def test_TC019_PCN_CompletedCoreCE_Assessment(self, setup, TestData):
        # [strJPNID, strgetData1,strDate] = self.test_TC018_PCN_Reassign_Assessment(setup, TestData)
        objCommon.LoadURL(MyConfigFiles.AppURL)
        objLogin.PCN_Login(TestData['UserName'], TestData['Password'])
        objSwitchToRoles.SwitchToRole("Context CE")
        objCreateJPCN.CreateJPCN(TestData['SupplierName'])
        strDate = objCreateJPCN.PCN_DateSelections(TestData['PCN_EffDays'], TestData['PCNTYPE'], TestData['LT_BuyDays'], TestData['LT_ShipDays'])
        [strJPNID, strgetData1] = objCreateJPCN.PDNinfo_form(TestData['PCNSource'], TestData['Natureofchange'], TestData['Typeofchange'])
        objCreateJPCN.JPN_MPN_Info('MaximSupplierStatus1')
        objCreateJPCN.Uploadvalidation()
        objJPCNStatusOverview.ClickContextCE_Create_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_BackButton_Navigation()
        objCreateJPCN.Edit_EnterPCNDetails_Page()
        objCreateJPCN.EOL_InvistigationFileUpload_fromJPNTable1('EOL-Investigation-Form')
        objCreateJPCN.EOL_Upload_Validations(TestData['strResponsibleCoreCE'])
        objCreateJPCN.GetCoreCENames()
        objCreateJPCN.GetCommodityGroups()
        objCreateJPCN.readExcelData_Compare_SupplierStatus('SupplierMapping', TestData['SupplierName'])
        objCreateJPCN.AddNewAttachement_JPNMPN(TestData['strCategory'], 'MPN4', 'enter')
        objCreateJPCN.DeleteAttachement()
        objCreateJPCN.PreviewScreen_Validations()
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section()
        objCreateJPCN.WhereUserAnalysis(TestData['PCNTYPE'], TestData['strCategory'], 'MPN4', 'enter')
        objJPCNStatusOverview.ClickContextCE_InitialAssessment_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section()
        objInitalAssessment.InitialAssessment_ContextCE_Details(TestData['CCER'], TestData['priorityType'], TestData['PCNTYPE'], TestData['ASQNeeded'])
        objInitalAssessment.InitialAssessment_AddNewRecord(TestData['DeviationStatus'], TestData['MCOECO'])
        objInitalAssessment.QualDataReview_Attachement('QualReport', TestData['QualReportStatus'])
        objInitalAssessment.InitialAssessment_Checking_AutoPopulationOfPCNCompliance(TestData['PCNTYPE'],  strDate['EFRCDiff'], strDate['BRDiff'], strDate['SBDiff'],
                                                                                     TestData['ReasonforNC'])
        objInitalAssessment.Complete_Assessment()
        objSwitchToRoles.SwitchToRole("Core CE")
        objJPCNStatusOverview.ClickDashboard_Link()
        objJPCNStatusOverview.ClickCoreCE_AssesmnetPending_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objJPCNStatusOverview.SendBack_with_AssignBacktoContextCE(TestData['AssginbackComments'])
        objSwitchToRoles.SwitchToRole("Context CE")
        objJPCNStatusOverview.ClickDashboard_Link()
        objJPCNStatusOverview.Reassign_Assessment()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section()
        objInitalAssessment.InitialAssessment_AddNewRecord(TestData['DeviationStatus'], TestData['MCOECO'])
        objInitalAssessment.Complete_Assessment()
        objSwitchToRoles.SwitchToRole("Core CE")
        objJPCNStatusOverview.ClickDashboard_Link()
        objJPCNStatusOverview.ClickCoreCE_AssesmnetPending_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section()
        objInitalAssessment.InitialAssessment_AddNewRecord(TestData['DeviationStatus'], TestData['MCOECO'])
        objCreateJPCN.ClickOnJPN_MPN_Exapnd()
        objCreateJPCN.EOL_InvistigationFileUpload_fromJPNTable1('EOL-Investigation-Form')
        objCreateJPCN.DeleteAttachement_PRrows()
        objJPCNStatusOverview.Validation_OnCoreCE_ManadtoryFields('MPN4', TestData['QRAS'], TestData['QRRC'], TestData['CoreCERecommendations']
                                                                  , TestData['CoreCeREComments'], TestData['ReasonforNC'])
        objJPCNStatusOverview.Goabck_button()
        objJPCNStatusOverview.CoreCE_PCN_ChangeComplianceSelect_Validations(TestData['ReasonforNC'])
        objJPCNStatusOverview.Goabck_button()
        objInitalAssessment.Complete_Assessment()
        objInitalAssessment.Submit_OnWarringWindow()
        objLogin.PCN_LogOut()
        return strJPNID, strgetData1,strDate

    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    @pytest.mark.dependency(depends=["Test_PCN::test_TC019_PCN_CompletedCoreCE_Assessment"])
    def test_TC020_PCN_ContextCE_ClosureAssessment(self, setup, TestData):
        # [strJPNID, strgetData1,strDate] = self.test_TC019_PCN_CompletedCoreCE_Assessment(setup, TestData)
        objCommon.LoadURL(MyConfigFiles.AppURL)
        objLogin.PCN_Login(TestData['UserName'], TestData['Password'])
        objSwitchToRoles.SwitchToRole("Context CE")
        objCreateJPCN.CreateJPCN(TestData['SupplierName'])
        strDate = objCreateJPCN.PCN_DateSelections(TestData['PCN_EffDays'], TestData['PCNTYPE'], TestData['LT_BuyDays'], TestData['LT_ShipDays'])
        [strJPNID, strgetData1] = objCreateJPCN.PDNinfo_form(TestData['PCNSource'], TestData['Natureofchange'], TestData['Typeofchange'])
        objCreateJPCN.JPN_MPN_Info('MaximSupplierStatus1')
        objCreateJPCN.Uploadvalidation()
        objJPCNStatusOverview.ClickContextCE_Create_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_BackButton_Navigation()
        objCreateJPCN.Edit_EnterPCNDetails_Page()
        objCreateJPCN.EOL_InvistigationFileUpload_fromJPNTable1('EOL-Investigation-Form')
        objCreateJPCN.EOL_Upload_Validations(TestData['strResponsibleCoreCE'])
        objCreateJPCN.GetCoreCENames()
        objCreateJPCN.GetCommodityGroups()
        objCreateJPCN.readExcelData_Compare_SupplierStatus('SupplierMapping', TestData['SupplierName'])
        objCreateJPCN.AddNewAttachement_JPNMPN(TestData['strCategory'], 'MPN4', 'enter')
        objCreateJPCN.DeleteAttachement()
        objCreateJPCN.PreviewScreen_Validations()
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section()
        objCreateJPCN.WhereUserAnalysis(TestData['PCNTYPE'], TestData['strCategory'], 'MPN4', 'enter')
        objJPCNStatusOverview.ClickContextCE_InitialAssessment_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section()
        objInitalAssessment.InitialAssessment_ContextCE_Details(TestData['CCER'], TestData['priorityType'], TestData['PCNTYPE'], TestData['ASQNeeded'])
        objInitalAssessment.InitialAssessment_AddNewRecord(TestData['DeviationStatus'], TestData['MCOECO'])
        objInitalAssessment.QualDataReview_Attachement('QualReport', TestData['QualReportStatus'])
        objInitalAssessment.InitialAssessment_Checking_AutoPopulationOfPCNCompliance(TestData['PCNTYPE'], strDate['EFRCDiff'], strDate['BRDiff'], strDate['SBDiff'],
                                                                                     TestData['ReasonforNC'])
        objInitalAssessment.Complete_Assessment()
        objSwitchToRoles.SwitchToRole("Core CE")
        objJPCNStatusOverview.ClickDashboard_Link()
        objJPCNStatusOverview.ClickCoreCE_AssesmnetPending_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objJPCNStatusOverview.SendBack_with_AssignBacktoContextCE(TestData['AssginbackComments'])
        objSwitchToRoles.SwitchToRole("Context CE")
        objJPCNStatusOverview.ClickDashboard_Link()
        objJPCNStatusOverview.Reassign_Assessment()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section()
        objInitalAssessment.InitialAssessment_AddNewRecord(TestData['DeviationStatus'], TestData['MCOECO'])
        objInitalAssessment.Complete_Assessment()
        objSwitchToRoles.SwitchToRole("Core CE")
        objJPCNStatusOverview.ClickDashboard_Link()
        objJPCNStatusOverview.ClickCoreCE_AssesmnetPending_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section()
        objInitalAssessment.InitialAssessment_AddNewRecord(TestData['DeviationStatus'], TestData['MCOECO'])
        objCreateJPCN.ClickOnJPN_MPN_Exapnd()
        objCreateJPCN.EOL_InvistigationFileUpload_fromJPNTable1('EOL-Investigation-Form')
        objCreateJPCN.DeleteAttachement_PRrows()
        objJPCNStatusOverview.Validation_OnCoreCE_ManadtoryFields('MPN4', TestData['QRAS'], TestData['QRRC'], TestData['CoreCERecommendations'], TestData['CoreCeREComments'],
                                                                  TestData['ReasonforNC'])
        objJPCNStatusOverview.Goabck_button()
        objJPCNStatusOverview.CoreCE_PCN_ChangeComplianceSelect_Validations(TestData['ReasonforNC'])
        objJPCNStatusOverview.Goabck_button()
        objInitalAssessment.Complete_Assessment()
        objInitalAssessment.Submit_OnWarringWindow()
        objSwitchToRoles.SwitchToRole("Context CE")
        objJPCNStatusOverview.ClickDashboard_Link()
        objClosureAssessment.Closure_Assesement_DashBorad_Link()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objClosureAssessment.ValidationcheckFor_JPNMPNInfor_Section()
        objClosureAssessment.ValidationcheckFor_CONTEXTCE_DETAILS_Section_ClosureAssessment(TestData['PCNStatus_Reopen'])
        objClosureAssessment.ValidationcheckFor_CONTEXTCE_DETAILS_Section_ClosureAssessment(TestData['PCNStatus_Open'])
        objClosureAssessment.EDit_PR_Section_ClosureAssessment(TestData['PCNStatus_Closed'],  TestData['pcnComments'], TestData['pcnClosedComments'])
        objCompleteAssessment.Verify_CompleteAssessment(strJPNID)
        objLogin.PCN_LogOut()
        return strJPNID, strgetData1,strDate

    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    @pytest.mark.dependency(depends=["Test_PCN::test_TC002_PCN_CreateJPCN"])
    def test_TC021_PCN_SolvingMultiple_CoreCE_Problem_Duplicating(self, setup, TestData):
        # [strJPNID, strgetData1,strDate] = self.test_TC002_PCN_CreateJPCN(setup, TestData)
        objCommon.LoadURL(MyConfigFiles.AppURL)
        objLogin.PCN_Login(TestData['UserName'], TestData['Password'])
        objSwitchToRoles.SwitchToRole("Context CE")
        objCreateJPCN.CreateJPCN(TestData['SupplierName'])
        strDate = objCreateJPCN.PCN_DateSelections(TestData['PCN_EffDays'], TestData['PCNTYPE'], TestData['LT_BuyDays'],TestData['LT_ShipDays'])
        [strJPNID, strgetData1] = objCreateJPCN.PDNinfo_form(TestData['PCNSource'], TestData['Natureofchange'], TestData['Typeofchange'])
        objCreateJPCN.JPN_MPN_Info('MaximSupplierStatus1')
        objCreateJPCN.Uploadvalidation()
        objJPCNStatusOverview.ClickContextCE_Create_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.AddNewAttachement_JPNMPN(TestData['strCategory'], 'MPN4', 'enter')
        objCreateJPCN.MultipleCoreCE_Selection(strJPNID)
        objCreateJPCN.Verify_BackButton_Navigation()
        objData1=objCreateJPCN.get_EnterPCNDetails_all_data()
        objCreateJPCN.Compare_New_DuplicatedJPCN_EnterPCNDetails(strgetData1,objData1)
        objLogin.PCN_LogOut()
        return strJPNID, strgetData1, strDate



    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    @pytest.mark.dependency(depends=["Test_PCN::test_TC020_PCN_ContextCE_ClosureAssessment"])
    def test_TC022_PCN_ContextCE_ClosureAssessment_EOL(self, setup, TestData):
        # [strJPNID, strgetData1,strDate] = self.test_TC020_PCN_ContextCE_ClosureAssessment(setup, TestData)
        objCommon.LoadURL(MyConfigFiles.AppURL)
        objLogin.PCN_Login(TestData['UserName'], TestData['Password'])
        objSwitchToRoles.SwitchToRole("Context CE")
        objCreateJPCN.CreateJPCN(TestData['SupplierName'])
        strDate = objCreateJPCN.PCN_DateSelections(TestData['PCN_EffDays'], TestData['PCNTYPE'], TestData['LT_BuyDays'], TestData['LT_ShipDays'])
        [strJPNID, strgetData1] = objCreateJPCN.PDNinfo_form(TestData['PCNSource'], TestData['Natureofchange'],  TestData['Typeofchange'])
        objCreateJPCN.JPN_MPN_Info('MaximSupplierStatus1')
        objCreateJPCN.Uploadvalidation()
        objJPCNStatusOverview.ClickContextCE_Create_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_BackButton_Navigation()
        objCreateJPCN.Edit_EnterPCNDetails_Page()
        objCreateJPCN.EOL_InvistigationFileUpload_fromJPNTable1('EOL-Investigation-Form')
        objCreateJPCN.EOL_Upload_Validations(TestData['strResponsibleCoreCE'])
        objCreateJPCN.GetCoreCENames()
        objCreateJPCN.GetCommodityGroups()
        objCreateJPCN.readExcelData_Compare_SupplierStatus('SupplierMapping', TestData['SupplierName'])
        objCreateJPCN.AddNewAttachement_JPNMPN(TestData['strCategory'], 'MPN4', 'enter')
        objCreateJPCN.DeleteAttachement()
        objCreateJPCN.PreviewScreen_Validations()
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section()
        objCreateJPCN.WhereUserAnalysis(TestData['PCNTYPE'], TestData['strCategory'], 'MPN4', 'enter')
        objJPCNStatusOverview.ClickContextCE_InitialAssessment_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section()
        objInitalAssessment.InitialAssessment_ContextCE_Details(TestData['CCER'], TestData['priorityType'], TestData['PCNTYPE'], TestData['ASQNeeded'])
        objInitalAssessment.InitialAssessment_AddNewRecord(TestData['DeviationStatus'], TestData['MCOECO'])
        objInitalAssessment.QualDataReview_Attachement('QualReport', TestData['QualReportStatus'])
        objInitalAssessment.InitialAssessment_Checking_AutoPopulationOfPCNCompliance(TestData['PCNTYPE'],  strDate['EFRCDiff'], strDate['BRDiff'], strDate['SBDiff'],
                                                                                     TestData['ReasonforNC'])
        objInitalAssessment.Complete_Assessment()
        objSwitchToRoles.SwitchToRole("Core CE")
        objJPCNStatusOverview.ClickDashboard_Link()
        objJPCNStatusOverview.ClickCoreCE_AssesmnetPending_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objJPCNStatusOverview.SendBack_with_AssignBacktoContextCE(TestData['AssginbackComments'])
        objSwitchToRoles.SwitchToRole("Context CE")
        objJPCNStatusOverview.ClickDashboard_Link()
        objJPCNStatusOverview.Reassign_Assessment()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section()
        objInitalAssessment.InitialAssessment_AddNewRecord(TestData['DeviationStatus'], TestData['MCOECO'])
        objInitalAssessment.Complete_Assessment()
        objSwitchToRoles.SwitchToRole("Core CE")
        objJPCNStatusOverview.ClickDashboard_Link()
        objJPCNStatusOverview.ClickCoreCE_AssesmnetPending_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section()
        objInitalAssessment.InitialAssessment_AddNewRecord(TestData['DeviationStatus'], TestData['MCOECO'])
        objCreateJPCN.ClickOnJPN_MPN_Exapnd()
        objCreateJPCN.EOL_InvistigationFileUpload_fromJPNTable1('EOL-Investigation-Form')
        objCreateJPCN.DeleteAttachement_PRrows()
        objJPCNStatusOverview.Validation_OnCoreCE_ManadtoryFields('MPN4', TestData['QRAS'], TestData['QRRC'], TestData['CoreCERecommendations'], TestData['CoreCeREComments'],
                                                                  TestData['ReasonforNC'])
        objJPCNStatusOverview.Goabck_button()
        objJPCNStatusOverview.CoreCE_PCN_ChangeComplianceSelect_Validations(TestData['ReasonforNC'])
        objJPCNStatusOverview.Goabck_button()
        objInitalAssessment.Complete_Assessment()
        objInitalAssessment.Submit_OnWarringWindow()
        objSwitchToRoles.SwitchToRole("Context CE")
        objJPCNStatusOverview.ClickDashboard_Link()
        objClosureAssessment.Closure_Assesement_DashBorad_Link()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objClosureAssessment.ValidationcheckFor_JPNMPNInfor_Section()
        objClosureAssessment.ValidationcheckFor_CONTEXTCE_DETAILS_Section_ClosureAssessment(TestData['PCNStatus_Reopen'])
        objClosureAssessment.ValidationcheckFor_CONTEXTCE_DETAILS_Section_ClosureAssessment(TestData['PCNStatus_Open'])
        objClosureAssessment.EDit_PR_Section_ClosureAssessment(TestData['PCNStatus_Closed'], TestData['pcnComments'], TestData['pcnClosedComments'])
        objCompleteAssessment.Verify_CompleteAssessment(strJPNID)
        objLogin.PCN_LogOut()
        return strJPNID, strgetData1,strDate

    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    @pytest.mark.dependency(depends=["Test_PCN::test_TC001_PCN_Switchtootherroles"])
    def test_TC023_PCN_Search_Results(self,setup, TestData):
        # self.test_TC001_PCN_Switchtootherroles(setup, TestData)
        objCommon.LoadURL(MyConfigFiles.AppURL)
        objLogin.PCN_Login(TestData['UserName'], TestData['Password'])
        objSwitchToRoles.SwitchToRole("Context CE")
        objHome.ClickSearchLnk()
        objSearch.Select_ResponsibleContextCE(TestData['strResponsibleCoreCE'])
        time.sleep(5)
        objSearch.Click_Search_Button()
        time.sleep(5)
        objSearch.Verify_Search_Results_ResContextCEName(TestData['UserName'])
        objLogin.PCN_LogOut()

    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    @pytest.mark.dependency(depends=["Test_PCN::test_TC023_PCN_Search_Results"])
    def test_TC024_PCN_Search_EditJPCN(self,setup, TestData):
        # self.test_TC023_PCN_Search_Results(setup, TestData)
        objCommon.LoadURL(MyConfigFiles.AppURL)
        objLogin.PCN_Login(TestData['UserName'], TestData['Password'])
        objSwitchToRoles.SwitchToRole("Context CE")
        objHome.ClickSearchLnk()
        objSearch.Select_ResponsibleContextCE(TestData['strResponsibleCoreCE'])
        time.sleep(5)
        objSearch.Click_Search_Button()
        time.sleep(5)
        objSearch.Verify_Search_Results_ResContextCEName(TestData['UserName'])
        objSearch.Search_For_ClosedPCN_And_ClickEditIcon()
        objSearch.Edit_PCNPDN_BySearch(TestData['DescriptionChange'],TestData['EditComments'])
        objCreateJPCN.AddNewAttachement_JPNMPN(TestData['strCategory'], 'MPN4', 'enter')
        objLogin.PCN_LogOut()

    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    @pytest.mark.dependency(depends=["Test_PCN::test_TC005_PCN_ProcessChange_Validations"])
    def test_TC025_PCN_Search_ReOpenJPCN(self, setup, TestData):
        # self.test_TC005_PCN_ProcessChange_Validations(setup, TestData)
        objCommon.LoadURL(MyConfigFiles.AppURL)
        objLogin.PCN_Login(TestData['UserName'], TestData['Password'])
        objSwitchToRoles.SwitchToRole("Context CE")
        objCreateJPCN.CreateJPCN(TestData['SupplierName'])
        strDate = objCreateJPCN.PCN_DateSelections(TestData['PCN_EffDays'], TestData['PCNTYPE'], TestData['LT_BuyDays'], TestData['LT_ShipDays'])
        [strJPNID, strgetData1] = objCreateJPCN.PDNinfo_form(TestData['PCNSource'], TestData['Natureofchange'], TestData['Typeofchange'])
        objCreateJPCN.JPN_MPN_Info('NoImpactFound1')
        objCreateJPCN.Uploadvalidation()
        objJPCNStatusOverview.ClickContextCE_Create_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.JPN_MPN_Info_ValidationCheck()
        objCreateJPCN.Validate_CCE_PrePoulated_Values()
        objCreateJPCN.Validate_InvalidPCN_Status(TestData['PCNStatus_Open'])
        objCreateJPCN.Validate_InvalidPCN_Status(TestData['PCNStatus_Reopen'])
        objCreateJPCN.ClosethisPCN(TestData['PCNStatus_Closed'])
        objHome.ClickSearchLnk()
        objSearch.Select_ResponsibleContextCE(TestData['strResponsibleCoreCE'])
        objSearch.Click_Search_Button()
        Closed_JPCNNumber=objSearch.Search_For_ClosedPCN_And_ClickReOpenIcon()
        objSearch.ReOpen_PCNPDN_BySearch()
        objJPCNStatusOverview.SelectJCPN(Closed_JPCNNumber)
        objLogin.PCN_LogOut()
        return strJPNID, strgetData1, strDate

    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    @pytest.mark.dependency(depends=["Test_PCN::test_TC023_PCN_Search_Results"])
    def test_TC026_PCN_Search_DuplicatingJPCN(self, setup, TestData):
        # self.test_TC023_PCN_Search_Results(setup, TestData)
        time.sleep(5)
        objCommon.LoadURL(MyConfigFiles.AppURL)
        objLogin.PCN_Login(TestData['UserName'], TestData['Password'])
        objSwitchToRoles.SwitchToRole("Context CE")
        objHome.ClickSearchLnk()
        objSearch.Select_ResponsibleContextCE(TestData['strResponsibleCoreCE'])
        time.sleep(5)
        objSearch.Click_Search_Button()
        time.sleep(5)
        objSearch.Verify_Search_Results_ResContextCEName(TestData['UserName'])
        objData1=objSearch.Search_For_ClosedPCN_And_ClickDuplicatingJPCNIcon()
        JPCN_Number = objSearch.Duplicating_PCNPDN_BySearch()
        objJPCNStatusOverview.ClickDashboard_Link()
        objJPCNStatusOverview.ClickContextCE_Create_Items()
        objJPCNStatusOverview.SelectJCPN(JPCN_Number)
        objCreateJPCN.Verify_BackButton_Navigation()
        strgetData1 = objCreateJPCN.get_EnterPCNDetails_all_data()
        objCreateJPCN.Compare_New_DuplicatedJPCN_EnterPCNDetails(strgetData1, objData1)
        objLogin.PCN_LogOut()
        return JPCN_Number

    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    @pytest.mark.dependency(depends=["Test_PCN::test_TC002_PCN_CreateJPCN"])
    def test_TC027_PCN_SolvingMultiple_CoreCE_Problem_EditSameJPCN(self, setup, TestData):
        # [strJPNID, strgetData1, strDate] = self.test_TC002_PCN_CreateJPCN(setup, TestData)
        objCommon.LoadURL(MyConfigFiles.AppURL)
        objLogin.PCN_Login(TestData['UserName'], TestData['Password'])
        objSwitchToRoles.SwitchToRole("Context CE")
        objCreateJPCN.CreateJPCN(TestData['SupplierName'])
        strDate = objCreateJPCN.PCN_DateSelections(TestData['PCN_EffDays'], TestData['PCNTYPE'], TestData['LT_BuyDays'], TestData['LT_ShipDays'])
        [strJPNID, strgetData1] = objCreateJPCN.PDNinfo_form(TestData['PCNSource'], TestData['Natureofchange'], TestData['Typeofchange'])
        objCreateJPCN.JPN_MPN_Info('MaximSupplierStatus1')
        objCreateJPCN.Uploadvalidation()
        objJPCNStatusOverview.ClickContextCE_Create_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.AddNewAttachement_JPNMPN(TestData['strCategory'], 'MPN4', 'enter')
        objCreateJPCN.MultipleCoreCE_Selection_with_EDitCurrentJPCN(strJPNID)
        objCreateJPCN.PreviewScreen_Validations()
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section()
        objCreateJPCN.WhereUserAnalysis(TestData['PCNTYPE'], TestData['strCategory'], 'MPN4', 'enter')
        objLogin.PCN_LogOut()
        return strJPNID, strgetData1, strDate

    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    @pytest.mark.dependency(depends=["Test_PCN::test_TC008_PCN_CreatePCN_For_PCNTYPE_Process_Change"])
    def test_TC028_PCN_Update_COMMODITYMANAGER_JPNMPN_info_Table(self, setup, TestData):
        # [strJPNID, strgetData1,strDate]=self.test_TC008_PCN_CreatePCN_For_PCNTYPE_Process_Change(setup, TestData)
        objCommon.LoadURL(MyConfigFiles.AppURL)
        objLogin.PCN_Login(TestData['UserName'], TestData['Password'])
        objSwitchToRoles.SwitchToRole("Context CE")
        objCreateJPCN.CreateJPCN(TestData['SupplierName'])
        strDate = objCreateJPCN.PCN_DateSelections(TestData['PCN_EffDays'], TestData['PCNTYPE'], TestData['LT_BuyDays'], TestData['LT_ShipDays'])
        [strJPNID, strgetData1] = objCreateJPCN.PDNinfo_form(TestData['PCNSource'], TestData['Natureofchange'], TestData['Typeofchange'])
        objCreateJPCN.JPN_MPN_Info('MaximSupplierStatus1')
        objCreateJPCN.Uploadvalidation()
        objJPCNStatusOverview.ClickContextCE_Create_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_BackButton_Navigation()
        objCreateJPCN.Edit_EnterPCNDetails_Page()
        objCreateJPCN.EOL_InvistigationFileUpload_fromJPNTable1('EOL-Investigation-Form')
        objCreateJPCN.EOL_Upload_Validations(TestData['strResponsibleCoreCE'])
        objCreateJPCN.GetCoreCENames()
        objCreateJPCN.GetCommodityGroups()
        objCreateJPCN.readExcelData_Compare_SupplierStatus('SupplierMapping', TestData['SupplierName'])
        objCreateJPCN.AddNewAttachement_JPNMPN(TestData['strCategory'], 'MPN4', 'enter')
        objCreateJPCN.DeleteAttachement()
        objCreateJPCN.PreviewScreen_Validations()
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section()
        objCreateJPCN.WhereUserAnalysis(TestData['PCNTYPE'], TestData['strCategory'], 'MPN4', 'enter')
        objMysql.DB_Connections_execute(TestData['db_host'],TestData['db_username'], TestData['db_password'], TestData['UserName'], TestData['strResponsibleCoreCE'], strJPNID[-6:] )
        objLogin.PCN_LogOut()
        return strJPNID, strgetData1, strDate


    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.dependency()
    # @pytest.mark.dependency(depends=["Test_PCN::test_TC008_PCN_CreatePCN_For_PCNTYPE_Process_Change"])
    def test_TC029_PCN_GCM_Dashboard_Verification(self, setup, TestData):
        # [strJPNID, strgetData1, strDate] = self.test_TC028_PCN_Update_COMMODITYMANAGER_JPNMPN_info_Table(setup, TestData)
        objCommon.LoadURL(MyConfigFiles.AppURL)
        objLogin.PCN_Login(TestData['UserName'], TestData['Password'])
        objSwitchToRoles.SwitchToRole("Context CE")
        objCreateJPCN.CreateJPCN(TestData['SupplierName'])
        strDate = objCreateJPCN.PCN_DateSelections(TestData['PCN_EffDays'], TestData['PCNTYPE'], TestData['LT_BuyDays'], TestData['LT_ShipDays'])
        [strJPNID, strgetData1] = objCreateJPCN.PDNinfo_form(TestData['PCNSource'], TestData['Natureofchange'],  TestData['Typeofchange'])
        objCreateJPCN.JPN_MPN_Info('MaximSupplierStatus1')
        objCreateJPCN.Uploadvalidation()
        objJPCNStatusOverview.ClickContextCE_Create_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCreateJPCN.Verify_BackButton_Navigation()
        objCreateJPCN.Edit_EnterPCNDetails_Page()
        objCreateJPCN.EOL_InvistigationFileUpload_fromJPNTable1('EOL-Investigation-Form')
        objCreateJPCN.EOL_Upload_Validations(TestData['strResponsibleCoreCE'])
        objCreateJPCN.GetCoreCENames()
        objCreateJPCN.GetCommodityGroups()
        objCreateJPCN.readExcelData_Compare_SupplierStatus('SupplierMapping', TestData['SupplierName'])
        objCreateJPCN.AddNewAttachement_JPNMPN(TestData['strCategory'], 'MPN4', 'enter')
        objCreateJPCN.DeleteAttachement()
        objCreateJPCN.PreviewScreen_Validations()
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section()
        objCreateJPCN.WhereUserAnalysis(TestData['PCNTYPE'], TestData['strCategory'], 'MPN4', 'enter')
        objMysql.DB_Connections_execute(TestData['db_host'], TestData['db_username'], TestData['db_password'],
                                        TestData['UserName'], TestData['strResponsibleCoreCE'], strJPNID[-6:])
        objSwitchToRoles.SwitchToRole("Global Commodity Manager")
        objJPCNStatusOverview.ClickDashboard_Link()
        objInitalAssessment.Verify_GCM_DashBoard(strJPNID)
        objSwitchToRoles.SwitchToRole("Context CE")
        objJPCNStatusOverview.ClickDashboard_Link()
        objJPCNStatusOverview.ClickContextCE_InitialAssessment_Items()
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objInitalAssessment.InitialAssessment_ContextCE_Details(TestData['CCER'], TestData['priorityType'],TestData['PCNTYPE'], TestData['ASQNeeded'])
        objInitalAssessment.QualDataReview_Attachement('QualReport', TestData['QualReportStatus'])
        objInitalAssessment.InitialAssessment_Checking_AutoPopulationOfPCNCompliance(TestData['PCNTYPE'], strDate['EFRCDiff'],strDate['BRDiff'], strDate['SBDiff'],TestData['ReasonforNC'])
        objInitalAssessment.Complete_Assessment()
        objSwitchToRoles.SwitchToRole("Global Commodity Manager")
        objJPCNStatusOverview.ClickDashboard_Link()
        objJPCNStatusOverview.Verify_Save_For_Commodity_Manager(strJPNID)
        objJPCNStatusOverview.Verify_GCMTable_SignoffComments()
        objJPCNStatusOverview.Verify_Close_For_Commodity_Manager(strJPNID)
        objCreateJPCN.Verify_SupplierInfo_Edit_ProductData_Section()
        objCreateJPCN.Verify__PCN_PDNinfo_Edit_ProductData_Section()
        objInitalAssessment.InitialAssessment_AddNewRecord(TestData['DeviationStatus'], TestData['MCOECO'])
        objJPCNStatusOverview.Validation_OnCoreCE_ManadtoryFields('MPN4', TestData['QRAS'], TestData['QRRC'],TestData['CoreCERecommendations'] ,TestData['CoreCeREComments'],
                                                                  TestData['ReasonforNC'])
        objInitalAssessment.Submit_OnWarringWindow()
        objLogin.PCN_LogOut()
        return strJPNID, strgetData1, strDate









































