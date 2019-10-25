from QA.PageObjects.Test_Locators import QET
from QA.Utilities.PerformAction import PerformActions
from QA.Utilities.CommonLib import CommonFunctions
from QA.Base.Config import MyConfigFiles
from QA.BusinessLogic.Filter_Page import Filter
from QA.BusinessLogic.Home_Page import Home


import time

class createQI_Page():
    global objCommon, objActions,objHome,objFilter
    objCommon = CommonFunctions()
    objActions = PerformActions()
    objFilter = Filter()
    objHome = Home()
    def CreateQI(Self,Title,ProblemDescription,UserGroup,DisruptionType,RootcauseOwner,RootcauseType,EvidenceofDefect,HowDetected
                 ,impactedCustomer,tags,AffectedMfgSiteCode,Priority):
        objDic = dict();
        # click on QI Link
        time.sleep(5)
        objHome.ClickQIButton()
        time.sleep(4)
        objFilter.ClickCreate()
        # objActions.clickElement(QET.QIs_link_xpath, "xpath")
        # objCommon.capture_screenshot('Clicked on QI Link')
        # time.sleep(4)
        # objActions.clickElement(QET.Create_QI_button_xpath, "xpath")
        time.sleep(5)
        objActions.enterText(QET.Title_WebEdit_name, "name", Title)
        objActions.enterText(QET.ProblemDescription_WebEdit_name, "name", ProblemDescription)
        objActions.selectDropdown(QET.UserGroup_SelectBox_xpath, "xpath", "value", UserGroup)
        objActions.selectDropdown(QET.DisruptionType_Initial_SelectBox_xpath, "xpath", "visibletext", DisruptionType)
        objActions.selectDropdown(QET.RcOwner_Initial_SelectBox_name, "name", "visibletext", RootcauseOwner)
        objActions.selectDropdown(QET.RcType_Initial_SelectBox_name, "name", "visibletext", RootcauseType)
        objActions.enterText(QET.Evidence_OfDefect_WebEdit_name, "name", EvidenceofDefect)
        objActions.enterText(QET.HowDetected_WebEdit_name, "name",HowDetected)
        objActions.enterText(QET.Impacted_Customer_WebEdit_name, "name", impactedCustomer)
        objActions.enterText(QET.Tags_WebEdit_name, "name",tags)
        time.sleep(2)
        objActions.selectDropdown(QET.AffSite_Code_SelectBox_name, "name", "visibletext", AffectedMfgSiteCode)
        objActions.selectDropdown(QET.Priority_SelectBox_name, "name", "visibletext", Priority)
        objActions.clickElement(QET.CreateQI_button_xpath, "xpath")
        objCommon.capture_screenshot('QI Created Successfully')
        strQIID = objActions.getText(QET.QIID_WebElement_xpath, "xpath")
        print("QI Created successfully with ID:" + strQIID)
        objActions.getText(QET.QI_TimeLine_QIcreated_WebElement_xpath, "xpath")
        assert(objActions.AssertObjectExists(QET.QI_TimeLine_QIcreated_WebElement_xpath, "xpath"))
        strURL = objActions.getURL()
        objDic['URL'] = strURL
        objDic['QIID'] = strQIID
        return objDic




        # QI Edit flow with Affected and Impact analyis sections.
    def EditQI(self,DisruptionTypeCurrent,RootcauseOwnerCurrent,RootcauseTypeCurrent,QITeam,JNPRAssembly,JNPRComponents,
               FieldSeverityLevel,FieldCostImpact,ImpactDescription,Reference,ManufacturingSeverityLevel,
               ManufacturingCostImpact,JnprImpactDescription,ManufacturingReferences):
        # objFilter.NavigateToQI(QIID)
        time.sleep(3)
        objActions.clickElement(QET.EditQI_WebElement_xpath, "xpath")
        objActions.selectDropdown(QET.Disruption_TypeCurrent_SelectBox_name, "name", "visibletext", DisruptionTypeCurrent)
        objActions.selectDropdown(QET.RcOwner_Current_SelectBox_name, "name", "visibletext", RootcauseOwnerCurrent)
        objActions.clickElement(QET.Confirmation_button_xpath, "xpath")
        time.sleep(3)
        objActions.selectDropdown(QET.RcType_Current_SelectBox_name, "name", "visibletext", RootcauseTypeCurrent)
        objActions.enterText(QET.QI_Team_WebEdit_name, "name", QITeam)
        time.sleep(3)
        objActions.clickElement("//span[text()='" + QITeam + "']","xpath")
     #Affected Items info for Assembly
        objActions.clickElement(QET.Affecteditem_info_Expand_WebElement_name, "name")
        objActions.clickElement(QET.Affecteditem_assembly_WebElement_name, "name")
        objActions.enterText(QET.Jnpr_Assembly_WebEdit_name, "name", JNPRAssembly)
        time.sleep(3)
        objActions.clickElement("//li[text()='" + JNPRAssembly + "']","xpath")
        time.sleep(3)
        objActions.clickElement(QET.Jnpr_Assembly_Rev_WebElement_name, "name")
        objActions.clickElement(QET.Jnpr_AssemblyRev_WebElement_xpath, "xpath")
        objActions.clickElement(QET.Add_Assembly_parts_button_xpath, "xpath")
        objCommon.capture_screenshot('Affected assembly added Successfully')
     # Affected Items info for Componets
        objActions.clickElement(QET.Affecteditem_Components_WebElement_name, "name")
        objActions.enterText(QET.Jnpr_Components_WebEdit_name, "name",JNPRComponents)
        time.sleep(3)
        objActions.clickElement("//li[text()='" + JNPRComponents + "']","xpath")
        time.sleep(3)
        objActions.clickElement(QET.Jnpr_Components_WebElement_name, "name")
        objActions.clickElement(QET.Jnpr_Components_list_WebElement_xpath, "xpath")
        time.sleep(3)
        objActions.clickElement(QET.Add_Components_parts_button_xpath, "xpath")
        objCommon.capture_screenshot('Affected Componets added Successfully')
     # Impact Analyis Section
        objActions.clickElement(QET.IA_Expand_WebElement_name, "name")
        objActions.clickElement(QET.IA_FE_Checkbox_WebElement_name, "name")
        time.sleep(3)
        objActions.selectDropdown(QET.IA_FE_FSL_SelectBox_name, "name", "visibletext", FieldSeverityLevel)
        time.sleep(3)
        objActions.enterText(QET.IA_FE_FCI_WebEdit_name, "name", FieldCostImpact)
        objActions.enterText(QET.IA_FE_ID_WebEdit_name, "name", ImpactDescription)
        objActions.enterText(QET.IA_FE_REF_WebEdit_name, "name", Reference)
        objActions.clickElement(QET.IA_jnpr_MI_Checkbox_WebElement_name, "name")
        time.sleep(3)
        objActions.selectDropdown(QET.IA_Jnpr_MI_SelectBox_name, "name", "visibletext", ManufacturingSeverityLevel)
        objActions.enterText(QET.IA_Jnpr_MCI_WebEdit_name, "name", ManufacturingCostImpact)
        objActions.enterText(QET.IA_Jnpr_MID_WebEdit_name, "name", JnprImpactDescription)
        objActions.enterText(QET.IA_Jnpr_MRef_WebEdit_name, "name", ManufacturingReferences)
        objActions.clickElement(QET.CreateQI_button_xpath, "xpath")
        objCommon.capture_screenshot('Completed the Impacted analysis and Saved QI Successfully')

    # Affected items info selection- "ALL"
    def Affected_items_All_Selection(self):
        time.sleep(3)
        objActions.clickElement(QET.EditQI_WebElement_xpath, "xpath")
        objActions.clickElement(QET.Affecteditem_info_Expand_WebElement_name, "name")
        objActions.clickElement(QET.Affecteditem_assembly_ALL_WebElement_xpath, "xpath")
        objActions.clickElement(QET.Affecteditem_Components_ALL_WebElement_xpath, "xpath")
        objActions.clickElement(QET.CreateQI_button_xpath, "xpath")

    # Affected items info selection- "NONE"
    def Affected_items_None_Selection(self):
            time.sleep(3)
            objActions.clickElement(QET.EditQI_WebElement_xpath, "xpath")
            objActions.clickElement(QET.Affecteditem_info_Expand_WebElement_name, "name")
            objActions.clickElement(QET.Affecteditem_assembly_None_WebElement_xpath, "xpath")
            objActions.clickElement(QET.Affecteditem_Components_None_WebElement_xpath, "xpath")
            objActions.clickElement(QET.CreateQI_button_xpath, "xpath")

    def Begin_Cpahse_button(self,strTimestatus):
        time.sleep(2)
        objActions.clickElement(QET.QI_CBegin_Phase_WebElement_xpath, "xpath")
        time.sleep(2)
        # TmeLine_Status=objActions.getText(QET.QI_TimeLine_Containmentstarted_WebElement_xpath, "xpath")
        # print(TmeLine_Status)
        if strTimestatus == "Containment started":
            assert(objActions.AssertObjectExists(QET.QI_TimeLine_Containmentstarted_WebElement_xpath, "xpath"))
            objCommon.capture_screenshot("ContainmentStarted")
        else:
            objActions.getText(QET.QI_TimeLine_Validation_WebElement_xpath, "xpath")
            assert(objActions.AssertObjectExists(QET.QI_TimeLine_Validation_WebElement_xpath, "xpath"))
            objCommon.capture_screenshot("ValidationStarted")



    def ActionStatus(self, strActionTitle, status):
        time.sleep(4)
        strStatus = objActions.getText("//div[text()='" + strActionTitle + "']//following-sibling::div", "xpath")
        time.sleep(4)
        if strStatus == status:
            print("Passed- Action status is in " + strStatus)
        else:
            print("Action status is displaying" + strStatus + "instead of" + status)


     #ECD date Select function
    def ECD_DateSelection(self):
        time.sleep(2)
        objActions.clickElement(QET.QI_Phase_ECD_WebEdit_xpath, "xpath")
        intDay =objCommon.GetCurrentDay()
        strConcDate = "day-" + str(intDay)
        objActions.clickElement("//div[@aria-label='" + strConcDate + "']", "xpath")

    # Action Selections function
    def PhaseActions_select(self,AddAction,ActionsTitle,ActionDesc):
        time.sleep(2)
        objActions.selectDropdown(QET.QI_Action_SelectBox_xpath, "xpath", "visibletext", AddAction)
        objActions.enterText(QET.QI_CPhase_Manaction_Title_WebEdit_xpath, "xpath", ActionsTitle)
        objActions.enterText(QET.QI_CPhase_Manaction_Desc_WebEdit_xpath, "xpath", ActionDesc)

    def MarkASCompleteButton_click(self):
        # time.sleep(2)
        objActions.clickElement(QET.QI_Phase_action_MarkASCompleted_button_WebElement_xpath, "xpath")
        objActions.clickElement(QET.QI_Phase_action_MarkASConfirm_button_WebElement_xpath, "xpath")

    def Edit_Action(self,strActionTitle):
        # time.sleep(2)
        objActions.clickElement(QET.EditAction_button_xpath, "xpath")
        strUpdated_ActionTitle = "ok"
        objActions.enterText(QET.QI_CPhase_Manaction_Title_WebEdit_xpath, "xpath", strUpdated_ActionTitle)
        print("Title before update:" + strActionTitle)
        print("Title After update should be:" + strUpdated_ActionTitle)
        objActions.clickElement(QET.QI_Phase_Save_WebElement_xpath, "xpath")
        time.sleep(3)
        strUpdatedTitle = objActions.getText(QET.QI_ActionTitle_WebElement_xpath, "xpath")
        objCommon.capture_screenshot("Edited Action")
        time.sleep(3)
        self.ActionStatus(strUpdatedTitle, "In Progress")
        time.sleep(3)
        if strUpdatedTitle != strUpdated_ActionTitle:
            print("Successfully Edited Action title to-" + strUpdatedTitle)
        else:
            print("Could not Edit Containment to-" + strUpdatedTitle)
        assert strUpdatedTitle != strUpdated_ActionTitle

    def Delete_Action(self, strActionTitle):
        time.sleep(2)
        objActions.clickElement(QET.QI_Phase_action_Delete_button_WebElement_xpath, "xpath")
        objActions.clickElement(QET.QI_Phase_action_MarkASConfirm_button_WebElement_xpath, "xpath")
        time.sleep(3)
        objActions.ObjectExists("//div[text()='" + strActionTitle + "']", "xpath")



    def Manual_Action(self, ManualAddAction, strActionTitle, strActionDesc, Action):
        time.sleep(2)
        self.PhaseActions_select(ManualAddAction,strActionTitle,strActionDesc)
        time.sleep(2)
        self.ECD_DateSelection()
        objActions.clickElement(QET.QI_Phase_Save_WebElement_xpath,"xpath")
        time.sleep(3)
        self.ActionStatus(strActionTitle,"In Progress")
        time.sleep(2)
        if Action == 'Markascomplete':
            time.sleep(2)
            self.MarkASCompleteButton_click()
            objCommon.capture_screenshot("Manual action is completed")
            time.sleep(3)
        elif Action == 'Delete':
            self.Edit_Action(strActionTitle)
            # self.Delete_Action(strActionTitle)
            time.sleep(2)
            objActions.clickElement(QET.QI_Phase_action_Delete_button_WebElement_xpath, "xpath")
            objActions.clickElement(QET.QI_Phase_action_MarkASConfirm_button_WebElement_xpath, "xpath")
            time.sleep(2)
            objActions.ObjectExists("//div[text()='"+ strActionTitle +"']", "xpath")
            objCommon.capture_screenshot("Manual action is Deleted")
            # time.sleep(2)

    def Manual_Corrective_Action(self, ManualAddAction, strActionTitle, strActionDesc, Action):
        time.sleep(2)
        objActions.selectDropdown(QET.QI_CorrectiveAction_SelectBox_xpath, "xpath", "visibletext", ManualAddAction)
        objActions.enterText(QET.QI_CPhase_Manaction_Title_WebEdit_xpath, "xpath", strActionTitle)
        objActions.enterText(QET.QI_CPhase_Manaction_Desc_WebEdit_xpath, "xpath", strActionDesc)
        time.sleep(2)
        self.ECD_DateSelection()
        objActions.clickElement(QET.QI_Phase_Save_WebElement_xpath,"xpath")
        time.sleep(3)
        self.ActionStatus(strActionTitle,"In Progress")
        time.sleep(3)
        if Action == 'Markascomplete':
            time.sleep(2)
            self.MarkASCompleteButton_click()
            objCommon.capture_screenshot("Manual action is completed")
            time.sleep(3)
        elif Action == 'Delete' :
            self.Edit_Action(strActionTitle)
            # self.Delete_Action(strActionTitle)
            time.sleep(2)
            objActions.clickElement(QET.QI_Phase_action_Delete_button_WebElement_xpath, "xpath")
            objActions.clickElement(QET.QI_Phase_action_MarkASConfirm_button_WebElement_xpath, "xpath")
            time.sleep(4)
            objActions.ObjectExists("//div[text()='"+ strActionTitle +"']", "xpath")
            objCommon.capture_screenshot("Manual Corrective action is Deleted")
            time.sleep(3)



    def Purge_Action(self,PurgeAddAction,PurgeProduct,strActionTitle):
        time.sleep(3)
        objActions.selectDropdown(QET.QI_Action_SelectBox_xpath, "xpath", "visibletext", PurgeAddAction)
        objActions.clickElement(QET.QI_SplAction_Contiunepopup_WebElement_xpath, "xpath")
        time.sleep(3)
        self.ECD_DateSelection()
        objActions.selectDropdown(QET.QI_Purge_Product_SelectBox_xpath, "xpath", "visibletext", PurgeProduct)
        objActions.clickElement(QET.QI_Phase_Save_WebElement_xpath, "xpath")
        time.sleep(3)
        self.Edit_Action(strActionTitle)
        time.sleep(2)
        self.ValidationforPuge()
        # strPurgePRID=objActions.getText(QET.QI_Phase_Verfiy_PRID_Existing_WebElement_xpath, "xpath")
        # print("Purge Created successfully with PRID:" + strPurgePRID)
        # objActions.AssertObjectExists(QET.QI_Phase_Verfiy_PRID_Existing_WebElement_xpath, "xpath")
        # time.sleep(2)
        # strPurgePreAssForm = objActions.getText(QET.QI_Phase_Verfiy_PreAsscesmentForm_Existing_WebElement_xpath, "xpath")
        # print("Purge Created successfully with PreAssForm:" + strPurgePreAssForm)
        # objActions.AssertObjectExists(QET.QI_Phase_Verfiy_PreAsscesmentForm_Existing_WebElement_xpath, "xpath")
        # time.sleep(3)
        # strPurgeID = objActions.getText(QET.QI_Phase_Verfiy_PurgeID_Existing_WebElement_xpath, "xpath")
        # print("Purge Created successfully with PurgeID:" + strPurgeID)
        # objActions.AssertObjectExists(QET.QI_Phase_Verfiy_PurgeID_Existing_WebElement_xpath, "xpath")
        time.sleep(3)
        self.MarkASCompleteButton_click()
        objCommon.capture_screenshot("Purge- Actions status is Completed")

    def Purge_Corrective_Action(self,PurgeAddAction,PurgeProduct,strActionTitle):
        time.sleep(3)
        objActions.selectDropdown(QET.QI_CorrectiveAction_SelectBox_xpath, "xpath", "visibletext", PurgeAddAction)
        objActions.clickElement(QET.QI_SplAction_Contiunepopup_WebElement_xpath, "xpath")
        time.sleep(3)
        self.ECD_DateSelection()
        objActions.selectDropdown(QET.QI_Purge_Product_SelectBox_xpath, "xpath", "visibletext", PurgeProduct)
        objActions.clickElement(QET.QI_Phase_Save_WebElement_xpath, "xpath")
        time.sleep(3)
        self.Edit_Action(strActionTitle)
        time.sleep(2)
        self.ValidationforPuge()
        # objActions.AssertObjectExists(QET.QI_Phase_Verfiy_PRID_Existing_WebElement_xpath, "xpath")
        # objActions.AssertObjectExists(QET.QI_Phase_Verfiy_PreAsscesmentForm_Existing_WebElement_xpath, "xpath")
        # time.sleep(3)
        # objActions.AssertObjectExists(QET.QI_Phase_Verfiy_PurgeID_Existing_WebElement_xpath, "xpath")
        time.sleep(3)
        self.MarkASCompleteButton_click()
        objCommon.capture_screenshot("Purge- Actions status is Completed")

    def ValidationforPuge(self):
        strPurgePRID = objActions.getText(QET.QI_Phase_Verfiy_PRID_Existing_WebElement_xpath, "xpath")
        print("Purge Created successfully with PRID:" + strPurgePRID)
        objActions.AssertObjectExists(QET.QI_Phase_Verfiy_PRID_Existing_WebElement_xpath, "xpath")
        objActions.clickElement(QET.QI_Phase_Verfiy_PRID_Existing_WebElement_xpath, "xpath")
        # objCommon.GNATS_Naviagation()
        time.sleep(2)
        strPurgePreAssForm = objActions.getText(QET.QI_Phase_Verfiy_PreAsscesmentForm_Existing_WebElement_xpath, "xpath")
        print("Purge Created successfully with PreAssForm:" + strPurgePreAssForm)
        objActions.AssertObjectExists(QET.QI_Phase_Verfiy_PreAsscesmentForm_Existing_WebElement_xpath, "xpath")
        time.sleep(3)
        strPurgeID = objActions.getText(QET.QI_Phase_Verfiy_PurgeID_Existing_WebElement_xpath, "xpath")
        print("Purge Created successfully with PurgeID:" + strPurgeID)
        objActions.AssertObjectExists(QET.QI_Phase_Verfiy_PurgeID_Existing_WebElement_xpath, "xpath")
        objActions.clickElement(QET.QI_Phase_Verfiy_PurgeID_Existing_WebElement_xpath, "xpath")
        # objCommon.Agile_Naviagation()
        time.sleep(3)

    def StopShip_Action(self,StopShipAction,strActionTitle):
        time.sleep(2)
        objActions.selectDropdown(QET.QI_Action_SelectBox_xpath, "xpath", "visibletext", StopShipAction)
        objActions.clickElement(QET.QI_SplAction_Contiunepopup_WebElement_xpath, "xpath")
        time.sleep(2)
        self.ECD_DateSelection()
        time.sleep(2)
        objActions.clickElement(QET.QI_Phase_Save_WebElement_xpath, "xpath")
        time.sleep(2)
        # self.Edit_Action(strActionTitle)
        self.ValidationforSSID()
        time.sleep(3)
        self.MarkASCompleteButton_click()
        objCommon.capture_screenshot("Stop Ship Containment  - Action status is completed")
        time.sleep(2)

    def StopShip_Corrective_Action(self, StopShipAction, strActionTitle):
        time.sleep(2)
        objActions.selectDropdown(QET.QI_CorrectiveAction_SelectBox_xpath, "xpath", "visibletext", StopShipAction)
        objActions.clickElement(QET.QI_SplAction_Contiunepopup_WebElement_xpath, "xpath")
        time.sleep(2)
        self.ECD_DateSelection()
        time.sleep(2)
        objActions.clickElement(QET.QI_Phase_Save_WebElement_xpath, "xpath")
        time.sleep(3)
        # self.Edit_Action(strActionTitle)
        self.ValidationforSSID()
        time.sleep(3)
        self.MarkASCompleteButton_click()
        objCommon.capture_screenshot("Stop Ship - Action status is completed")
        time.sleep(2)

    def ValidationforSSID(self):
        SSID = objActions.getText(QET.QI_Verify_SSID_WebElemnt_xpath, "xpath")
        print("SS Actions Created successfully with SSID:" + SSID)
        objActions.AssertObjectExists(QET.QI_Verify_SSID_WebElemnt_xpath, "xpath")


        # Simple RCCA Rdaio selection
    def Resolutionpath_SimpleRCCA_Radio_selection(self):
        objActions.clickElement(QET.QI_Respath_WebElemet_xpath, "xpath")
        objActions.clickElement(QET.QI_Respath_SimpleRCCARadioSelection_WebElement_xpath, "xpath")
        objActions.clickElement(QET.QI_Respath_button_Ok_WebElement_xpath,"xpath")
        objActions.clickElement(QET.QI_Confimation_message_RCCAPhase_xpath, "xpath")
        assert(objActions.AssertObjectExists(QET.QI_TimeLine_RPSimpleRCCA_WebElement_xapth, "xpath"))
        assert(objActions.AssertObjectExists(QET.QI_TimeLine_RCCA_WebElement_xpath, "xpath"))
        objCommon.capture_screenshot("Simple RCCA is selected and not required validation phase")


        # Formal 8D Rdaio selection
    def Resolutionpath_Formal8D_Radio_selection(self,QITeam):
        objActions.clickElement(QET.QI_Respath_WebElemet_xpath, "xpath")
        objActions.clickElement(QET.QI_Respath_8DRadioSelection_WebElement_xpath, "xpath")
        objActions.clickElement(QET.QI_Respath_button_Ok_WebElement_xpath, "xpath")
        time.sleep(2)
        strErrorText=objActions.getText(QET.QI_Formal8D_error_withoutQIteam_xapth, "xpath")
        print(strErrorText)
        if strErrorText == "At least two members are required in the QI Team to begin an 8D. Please add members to the team before starting an 8D!":
            time.sleep(2)
            objActions.clickElement(QET.QI_Formal8D_Add2QI_WebElement_xapth, "xpath")
            time.sleep(2)
            objActions.clickElement(QET.EditQI_WebElement_xpath, "xpath")
            objActions.enterText(QET.QI_Team_WebEdit_name, "name", QITeam)
            objActions.clickElement("//span[text()='" + QITeam + "']", "xpath")
            time.sleep(2)
            objActions.clickElement(QET.CreateQI_button_xpath, "xpath")
            time.sleep(3)
            objActions.clickElement(QET.QI_Respath_WebElemet_xpath, "xpath")
            objActions.clickElement(QET.QI_Respath_8DRadioSelection_WebElement_xpath, "xpath")
            objActions.clickElement(QET.QI_Respath_button_Ok_WebElement_xpath, "xpath")
            objActions.clickElement(QET.QI_Confimation_message_RCCAPhase_xpath, "xpath")
            assert (objActions.AssertObjectExists(QET.QI_TimeLine_RP8D_WebElement_xpath, "xpath"))
            assert (objActions.AssertObjectExists(QET.QI_TimeLine_RCCA_WebElement_xpath, "xpath"))


        else:
            objActions.clickElement(QET.QI_Confimation_message_RCCAPhase_xpath, "xpath")
            assert (objActions.AssertObjectExists(QET.QI_TimeLine_RP8D_WebElement_xpath, "xpath"))
            assert (objActions.AssertObjectExists(QET.QI_TimeLine_RCCA_WebElement_xpath, "xpath"))

        # Close QI Rdaio selection
    def Resolutionpath_CloseQI_Radio_selection(self,ReasonforClosingQI):
        objActions.clickElement(QET.QI_Respath_WebElemet_xpath, "xpath")
        objActions.clickElement(QET.QI_Respath_CloseQIRadioSelection_WebElement_xpath, "xpath")
        objActions.clickElement(QET.QI_Respath_button_Ok_WebElement_xpath, "xpath")
        objActions.enterText(QET.QI_CloseQI_Reason_WebEdit_xpath, "xpath", ReasonforClosingQI)
        objActions.clickElement(QET.QI_Confimation_message_RCCAPhase_xpath, "xpath")
        objActions.getText(QET.QI_CloseQI_Status_xpath, "xpath")
        assert(objActions.AssertObjectExists(QET.QI_CloseQI_Status_xpath, "xpath"))
        objCommon.capture_screenshot("Sucessfuly capure the Closed QI status .")

        # Rootcause -Add 5 Why Analysis
    def RootCause_Add_5why_Action(self,FiveWHYAction,RootcasueTitle,ProblemStatement,Why1,Why2,Why3,Why4,Why5):
        time.sleep(2)
        objActions.selectDropdown(QET.QI_Action_SelectBox_xpath, "xpath", "visibletext", FiveWHYAction)
        objActions.enterText(QET.QI_RootCause_Title_WebEdit_xpath, "xpath" , RootcasueTitle)
        time.sleep(4)
        self.ECD_DateSelection()
        time.sleep(2)
        objActions.enterText(QET.QI_RootCause_5why_Probstatement_WebEdit_xpath, "xpath" , ProblemStatement)
        objActions.clickElement(QET.QI_RootCause_5why_AddNewWhy_WebElement_xpath, "xpath")
        objActions.enterText(QET.QI_RootCause_5why_why1_WebEdit_xpath, "xpath" , Why1)
        objActions.clickElement(QET.QI_RootCause_5why_AddNewWhy_WebElement_xpath, "xpath")
        objActions.enterText(QET.QI_RootCause_5why_why2_WebEdit_xpath, "xpath", Why2)
        objActions.clickElement(QET.QI_Phase_Save_WebElement_xpath, "xpath")
        objActions.clickElement(QET.EditAction_button_xpath, "xpath")
        objActions.clickElement(QET.QI_RootCause_5why_AddNewWhy_WebElement_xpath, "xpath")
        objActions.enterText(QET.QI_RootCause_5why_why3_WebEdit_xpath, "xpath", Why3)
        objActions.clickElement(QET.QI_RootCause_5why_AddNewWhy_WebElement_xpath, "xpath")
        objActions.enterText(QET.QI_RootCause_5why_why4_WebEdit_xpath, "xpath", Why4)
        objActions.clickElement(QET.QI_RootCause_5why_AddNewWhy_WebElement_xpath, "xpath")
        objActions.enterText(QET.QI_RootCause_5why_why5_WebEdit_xpath, "xpath", Why5)
        time.sleep(3)
        objActions.clickElement(QET.QI_Phase_Save_WebElement_xpath, "xpath")
        time.sleep(3)
        self.MarkASCompleteButton_click()
        objCommon.capture_screenshot("Five why analyis -Actions is completed")

        # Root cause Analyis - Finshbone Analyis
    def RootCause_Fishbone_Action(self,FishboneAnalysis,RootcasueTitle,FishProblemStatement,FishConclusion,Categoryone,Causeone,SecondCategory,SecondCause):
        time.sleep(2)
        objActions.selectDropdown(QET.QI_Action_SelectBox_xpath, "xpath", "visibletext", FishboneAnalysis)
        objActions.enterText(QET.QI_RootCause_Title_WebEdit_xpath, "xpath", RootcasueTitle)
        time.sleep(4)
        self.ECD_DateSelection()
        time.sleep(2)
        objActions.enterText(QET.QI_RootCause_Fishbone_ProblemStatement_WebEdit_xpath, "xpath", FishProblemStatement )
        objActions.enterText(QET.QI_RootCause_Fishbone_Conclusion_WebEdit_xpath, "xpath", FishConclusion)
        objActions.clickElement(QET.QI_Phase_Save_WebElement_xpath, "xpath")
        time.sleep(2)
        objActions.clickElement(QET.QI_Phase_action_MarkASCompleted_button_WebElement_xpath, "xpath")
        Strtext=objActions.getText(QET.QI_RootCause_Fishbone_ValidationMsg_xpath, "xpath")
        print(Strtext)
        #return Strtext
        time.sleep(2)
        objActions.AssertObjectExists(QET.QI_RootCause_Fishbone_ValidationMsg_xpath, "xpath")
        objCommon.capture_screenshot("Validation message is verified sucessfuly.")
        objActions.clickElement(QET.QI_RootCasue_Fishbone_ValiMsg_OK_WebElement_xpath, "xpath")
        time.sleep(2)
        objActions.clickElement(QET.EditAction_button_xpath, "xpath")
        objActions.clickElement(QET.QI_RootCause_Fishbone_AddNewCategory_WebElement_xpath, "xpath")
        objActions.enterText(QET.QI_RootCause_Fishbone_Categoryone_WebEdit_xpath, "xpath", Categoryone)
        objActions.clickElement(QET.QI_RootCause_Fishbone_AddNewCause_WebElement_xpath, "xpath")
        objActions.enterText(QET.QI_RootCause_Fishbone_CfCasef_WebEdit_xpath, "xpath", Causeone )
        time.sleep(3)
        objActions.clickElement(QET.QI_RootCause_Fishbone_AddNewCategory_WebElement_xpath, "xpath")
        objActions.enterText(QET.QI_RootCause_Fishbone_Categorytwo_WebEdit_xpath, "xpath", SecondCategory)
        objActions.clickElement(QET.QI_RootCause_Fishbone_AddNewcausetwo_WebElement_xpath, "xpath")
        objActions.enterText(QET.QI_RootCause_Fishbone_CsCases_WebEdit_xpath, "xpath", SecondCause)
        objActions.clickElement(QET.QI_Phase_Save_WebElement_xpath, "xpath")
        time.sleep(4)
        self.MarkASCompleteButton_click()
        objCommon.capture_screenshot("FishBone analysis - Actions is completed")



        #Corrective Action SCAR Action
    def Corrective_SCAR_Action(self,SCARAction,SCARSupplier,Jn_Escalation,Contact,Escalation,strActionTitle):
        time.sleep(2)
        objActions.selectDropdown(QET.QI_CorrectiveAction_SelectBox_xpath, "xpath", "visibletext", SCARAction)
        objActions.clickElement(QET.QI_SplAction_Contiunepopup_WebElement_xpath, "xpath")
        time.sleep(3)
        self.ECD_DateSelection()
        time.sleep(4)
        objActions.enterText(QET.Escalation_WebEdit_xpath, "xpath", Jn_Escalation)
        time.sleep(2)
        objActions.clickElement("//span[text()='" + Jn_Escalation + "']", "xpath")
        objActions.selectDropdown(QET.QI_Purge_Product_SelectBox_xpath, "xpath", "visibletext", SCARSupplier)
        objActions.selectDropdown(QET.Contact_SelectBox_xpath, "xpath", "visibletext", Contact)
        objActions.selectDropdown(QET.Escalation_SelectBox_xpath, "xpath", "visibletext", Escalation)
        objActions.clickElement(QET.QI_Phase_Save_WebElement_xpath, "xpath")
        time.sleep(3)
        self.Edit_Action(strActionTitle)
        strScarid=objActions.getText(QET.QI_CorrectiveActions_SCARID_webElement_xpath, "xpath")
        objActions.AssertObjectExists(QET.QI_CorrectiveActions_SCARID_webElement_xpath, "xpath")
        print("SCAR id created Sucessfully with ScarID:" +strScarid)
        time.sleep(3)
        self.MarkASCompleteButton_click()
        objCommon.capture_screenshot("SCAR -Actions is completed")



        # Corrective Action PR Action
    def PR_Action(self, PRAddAction, PRProduct,strActionTitle):
        time.sleep(2)
        objActions.selectDropdown(QET.QI_CorrectiveAction_SelectBox_xpath, "xpath", "visibletext", PRAddAction)
        time.sleep(3)
        objActions.clickElement(QET.QI_SplAction_Contiunepopup_WebElement_xpath, "xpath")
        self.ECD_DateSelection()
        time.sleep(3)
        objActions.selectDropdown(QET.QI_Purge_Product_SelectBox_xpath, "xpath", "visibletext", PRProduct)
        objActions.clickElement(QET.QI_Phase_Save_WebElement_xpath, "xpath")
        time.sleep(3)
        self.Edit_Action(strActionTitle)
        time.sleep(3)
        self.MarkASCompleteButton_click()
        objCommon.capture_screenshot("PR action is completed")




        # Preventive action
    def Preventive_Action(self, strActionTitle, strActionDesc,Action):
        time.sleep(3)
        objActions.clickElement(QET.AddCA_button_xpath, "xpath")
        objActions.enterText(QET.QI_CPhase_Manaction_Title_WebEdit_xpath, "xpath", strActionTitle)
        self.ECD_DateSelection()
        time.sleep(2)
        objActions.enterText(QET.QI_CPhase_Manaction_Desc_WebEdit_xpath, "xpath", strActionDesc)
        objActions.clickElement(QET.QI_Phase_Save_WebElement_xpath, "xpath")
        time.sleep(3)
        self.ActionStatus(strActionTitle, "In Progress")
        time.sleep(3)
        if Action == 'Markascomplete':
            time.sleep(3)
            self.MarkASCompleteButton_click()
            objCommon.capture_screenshot("Preventive action is completed")
            time.sleep(3)
        elif Action == 'Delete':
            self.Edit_Action(strActionTitle)
            # self.Delete_Action(strActionTitle)
            objActions.clickElement(QET.QI_Phase_action_Delete_button_WebElement_xpath, "xpath")
            objActions.clickElement(QET.QI_Phase_action_MarkASConfirm_button_WebElement_xpath, "xpath")
            time.sleep(3)
            objActions.ObjectExists("//div[text()='" + strActionTitle + "']", "xpath")
            objCommon.capture_screenshot("Preventive action is Deleted")
            time.sleep(2)
            strvalidation = objActions.getText(QET.QI_Validation_Notrequired_WebElement_xpath, "xpath")
            print(strvalidation)


        # Complete QI
    def Complete_QI (self,ReasonforClosingQI):
        time.sleep(2)
        objActions.clickElement(QET.QI_Complete_QI_button_xpath,"xpath")
        objActions.enterText(QET.QI_CloseQI_Reason_WebEdit_xpath, "xpath", ReasonforClosingQI)
        objActions.clickElement(QET.QI_Confimation_message_RCCAPhase_xpath, "xpath")
        objActions.getText(QET.QI_TimeLine_QICompleted_WebElement_xpath, "xpath")
        assert (objActions.AssertObjectExists(QET.QI_TimeLine_QICompleted_WebElement_xpath, "xpath"))
        objActions.getText(QET.QI_CloseQI_Status_xpath, "xpath")
        objActions.AssertObjectExists(QET.QI_CloseQI_Status_xpath, "xpath")
        objCommon.capture_screenshot("Sucessfuly capure completed QI and the Closed QI status .")

    def Close_QI(self, ReasonforClosingQI):
            time.sleep(2)
            objActions.clickElement(QET.QI_Cancel_QI_button_xpath, "xpath")
            objActions.enterText(QET.QI_CloseQI_Reason_WebEdit_xpath, "xpath", ReasonforClosingQI)
            objActions.clickElement(QET.QI_Confimation_message_RCCAPhase_xpath, "xpath")
            objActions.getText(QET.QI_CloseQI_Status_xpath, "xpath")
            objActions.AssertObjectExists(QET.QI_CloseQI_Status_xpath, "xpath")
            objCommon.capture_screenshot("Sucessfuly capure Cancel QI and the Closed QI status .")






















# def Existing_QI_Click(self,Status,JUNIPEROWNER):
#     time.sleep(4)
#     objActions.clickElement(QET.QIs_link_xpath, "xpath")
#     CommonFunction.capture_screenshot('Clicked on QI Link')
#     time.sleep(4)
#     objActions.selectDropdown(QET.QI_Filter_Status_SelectBox_xpath, "xpath", "visibletext", Status)
#     objActions.enterText(QET.QI_Filter_JNPROwner_WebEdit_xpath, "xpath", JUNIPEROWNER)
#     objActions.clickElement(QET.QI_Filter_Apply_WebElement_xpath, "xpath")
#     objActions.clickElement(QET.QI_Existing_QIID_WebElement_xpath, "xpath")
#     time.sleep(5)
#     objActions.clickElement(QET.EditQI_WebElement_xpath, "xpath")




