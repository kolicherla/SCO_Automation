class QET():
#SCAR Module
#QET Login page objects
    username_textbox_id = "userid"
    password_textbox_id = "password"
    submit_button_xpath = "//button[@type='submit']"
    logout_link_xpath = "//a[@href='/saml/logout']"

#QET Home Page
    SCARs_link_xpath = "//a[text()='SCARs']"


#SCAR Home page
    Create_button_xpath = "//button[@class='success margin-right-small']"
    ProblemDescription_WebEdit_xpath="//legend[contains(text(),'Problem Description')]/..//textarea"
    AffectedPart_webEdit_xpath="(//th[text()='Affected Part']/../../../..//input[@data-id='0'])[1]"
    AffectedPart_DropDown_xpath="'//li[@data-part='+TestData['AffectedPart']'"      #dynamic
    UserGroup_SelectBox_xpath="(//select)[1]"
    Supplier_SelectBox_xpath="(//select)[2]"
    Contact_SelectBox_xpath="//select[@class='margin-bottom' and @data-type='contact']"
    Escalation_SelectBox_xpath="//select[@class='margin-bottom' and @data-type='escalation']"
    Escalation_WebEdit_xpath="//input[@name='escaList']"
    SupplierWatchList_WebEdit_xpath="//select[@class='margin-bottom' and @data-type='watchlist']"
    CreateScar_button_xpath="//button[@class='success']"
    ScarID_WebElement_xpath="//*[@class='font-size-xlarge margin-top']/b"

#QI Module

#QET Home Page
    QIs_link_xpath = "//a[contains(text(),'QIs')]"


#QI Home page
    Create_QI_button_xpath = "//button[@class='success margin-right-small']"
    Title_WebEdit_name = "qiTitle"
    ProblemDescription_WebEdit_name ="problemDesc"
    UserGroup_SelectBox_xpath ="//select[@name='userGroup']"
    DisruptionType_Initial_SelectBox_xpath = "//select[@name='disruptionTypeInitial']"
    RcOwner_Initial_SelectBox_name = "rcOwnerInitial"
    RcType_Initial_SelectBox_name = "rcTypeInitial"
    Evidence_OfDefect_WebEdit_name = "evidenceOfDefect"
    HowDetected_WebEdit_name = "howDetected"
    Impacted_Customer_WebEdit_name = "impactedCustomer"
    Tags_WebEdit_name = "tags"
    AffSite_Code_SelectBox_name ="affSiteCode"
    Priority_SelectBox_name = "priority"
    CreateQI_button_xpath = "//button[@class='success']"
    QIID_WebElement_xpath ="//*[@class='font-size-xlarge margin-top']/b"
    EditQI_WebElement_xpath ="//button[@class='primary margin-right-small']"
    Disruption_TypeCurrent_SelectBox_name="disruptionTypeCurrent"
    RcOwner_Current_SelectBox_name= "rcOwnerCurrent"
    Confirmation_button_xpath ="//button[@class='btn btn-default']"
    RcType_Current_SelectBox_name= "rcTypeCurrent"
    QI_Team_WebEdit_name="qiTeam"
# Affected Item Info Sections
    Affecteditem_info_Expand_WebElement_name="createQiAffectedItemsbutton"
    Affecteditem_assembly_WebElement_name="affectedAssemblies"
    Affecteditem_assembly_ALL_WebElement_xpath="(//label[contains(text(),'All')]//input)[1]"
    Affecteditem_assembly_None_WebElement_xpath="(//label[contains(text(),'None')]//input)[1]"
    Jnpr_Assembly_WebEdit_name= "jnprAssemblies"
    Jnpr_Assembly_Rev_WebElement_name="selectRevision"
    Jnpr_AssemblyRev_WebElement_xpath="//ul[@class='flat-list part-helper']//label[contains(text(),'All')]//input"
    Add_Assembly_parts_button_xpath="//button[@class='margin-top-smaller']"
    Affecteditem_Components_WebElement_name="affectedComponents"
    Affecteditem_Components_ALL_WebElement_xpath="(//label[contains(text(),'All')]//input)[2]"
    Affecteditem_Components_None_WebElement_xpath="(//label[contains(text(),'None')]//input)[2]"
    Jnpr_Components_WebEdit_name="jnprComponents"
    Jnpr_Components_WebElement_name="selectPart"
    Jnpr_Components_list_WebElement_xpath="//div[@class='col-6 well no-padding-top']//label[contains(text(),'All')]//input"
    Add_Components_parts_button_xpath ="(//button[@class='margin-top-smaller'])[2]"
# Impact Analyis Section
    IA_Expand_WebElement_name="createQiImpactAnalysisbutton"
    IA_FE_Checkbox_WebElement_name="fieldExposure"
    IA_FE_FSL_SelectBox_name="fieldSLevel"
    IA_FE_FCI_WebEdit_name="fieldCImpact"
    IA_FE_ID_WebEdit_name="fieldImpactDesc"
    IA_FE_REF_WebEdit_name="fieldReferences"
    IA_jnpr_MI_Checkbox_WebElement_name="jnprManufacturingImpact"
    IA_Jnpr_MI_SelectBox_name="manufacturingSLevel"
    IA_Jnpr_MCI_WebEdit_name="manufacturingCImpact"
    IA_Jnpr_MID_WebEdit_name="manufacturingImpactDesc"
    IA_Jnpr_MRef_WebEdit_name="manufacturingReferences"
    CreateQI_button_xpath = "//button[@class='success']"

# Simple_RCCA_ flow
    QI_CBegin_Phase_WebElement_xpath = "//button[@class='primary compact']"
    QI_Action_SelectBox_xpath = "//select[contains(@name,'add action')]"
    QI_CPhase_Manaction_Title_WebEdit_xpath="//fieldset[1]//input['text']"
    QI_Phase_ECD_WebEdit_xpath="//div[@class='react-datepicker__input-container']"#//fieldset
    QI_CPhase_Manaction_Desc_WebEdit_xpath="//div[@class='col-6']//fieldset//textarea"
    QI_Phase_Save_WebElement_xpath="//button[@class='success margin-right']"
    QI_Phase_action_MarkASCompleted_button_WebElement_xpath="//button[text()='Mark as Completed']"
    QI_Phase_action_Delete_button_WebElement_xpath="//button[text()='Delete']"
    QI_Phase_action_MarkASConfirm_button_WebElement_xpath="//button[@class='btn btn-default success margin-right']"

# Purge_flow
    QI_SplAction_Contiunepopup_WebElement_xpath="//button[@class='compact close-modal']"
    QI_Purge_ID_WebEdit_xpath="//fieldset[3]//input[1]"
    QI_Purge_Product_SelectBox_xpath="//div[@class='col-6']//div//fieldset//select"
    QI_Phase_Verfiy_PRID_Existing_WebElement_xpath="//a[contains(text(),'PR#')]"
    QI_Phase_Verfiy_PreAsscesmentForm_Existing_WebElement_xpath="//a[contains(text(),'Pre-assessment Form')]"
    QI_Phase_Verfiy_PurgeID_Existing_WebElement_xpath="//a[contains(text(),'Purge#')]"

# StopShip_flow
    QI_SHOPSHIP_ID_WebEdit_xpath="//fieldset[3]//input[1]"



# Resloutin Path
    QI_Respath_WebElemet_xpath="//p[contains(text(),'Resolution Path')]"
    QI_Respath_SimpleRCCARadioSelection_WebElement_xpath="//input[@value='rcca']"
    QI_Respath_8DRadioSelection_WebElement_xpath="//input[@value='eightD']"
    QI_Respath_CloseQIRadioSelection_WebElement_xpath="//input[@value='closeQi']"
    QI_Respath_button_Ok_WebElement_xpath="//button[@class='margin-right']"
    QI_Confimation_message_RCCAPhase_xpath="//button[@class='compact close-modal danger margin-right']"

# Rootcause Analysis Path
    QI_RootCause_Title_WebEdit_xpath="//div[@class='col-9']//section[@class='grid']//div[@class='col-9']//input"
    QI_RootCause_5why_Probstatement_WebEdit_xpath="//div[@class='padding-bottom']//input"
    QI_RootCause_5why_AddNewWhy_WebElement_xpath="//a[contains(text(),'+ Add New Why')]" #//div[@class='padding-left padding-right']/a[@href='javascript:void(0)']
    QI_RootCause_5why_why1_WebEdit_xpath="//div[@class='padding-left padding-right padding-bottom']//input"
    QI_RootCause_5why_why2_WebEdit_xpath="//div[4]//div[1]//input[1]"
    QI_RootCause_5why_why3_WebEdit_xpath="//div[@class='col-12 well supplier-widget']//div[5]//div[1]//input[1]"
    QI_RootCause_5why_why4_WebEdit_xpath="//div[6]//div[1]//input[1]"
    QI_RootCause_5why_why5_WebEdit_xpath="//div[7]//div[1]//input[1]"
    EditAction_button_xpath="//button[@class='margin-right margin-bottom primary'][text()='Edit']"
    QI_RootCause_Fishbone_ProblemStatement_WebEdit_xpath="//div[@class='padding-bottom-larger']//input"
    QI_RootCause_Fishbone_AddNewCategory_WebElement_xpath="//a[contains(text(),'+ Add New Category')]"
    QI_RootCause_Fishbone_Categoryone_WebEdit_xpath="//div[@class='padding-around']//div//input"
    QI_RootCause_Fishbone_AddNewCause_WebElement_xpath="//a[contains(text(),'+ Add New Cause')]"
    QI_RootCause_Fishbone_AddNewcausetwo_WebElement_xpath="(//a[text()='+ Add New Cause'])[2]"
    QI_RootCause_Fishbone_CfCasef_WebEdit_xpath="//div[@class='padding-left-larger padding-right padding-bottom']//input"
    QI_RootCause_Fishbone_Categorytwo_WebEdit_xpath="//div[@class='padding-around']//div[2]//input[1]"
    QI_RootCause_Fishbone_CsCases_WebEdit_xpath="//div[@class='padding-around']//div[2]//div[1]//div[1]//input[1]"
    QI_RootCause_Fishbone_Conclusion_WebEdit_xpath="//div[@class='padding-top-larger']//input"
    QI_RootCause_Fishbone_ValidationMsg_xpath="//div[@class='text-color-red margin-bottom align-center']"
    QI_RootCasue_Fishbone_ValiMsg_OK_WebElement_xpath="//button[contains(text(),'Ok')]"
    QI_CorrectiveActions_SCARID_webElement_xpath="//p[contains(text(),'SCAR-')]"
    QI_CorrectiveAction_SelectBox_xpath_="(//select[contains(@name,'add action')])[2]"
    QI_PreventiveAction_button_xpath="//button[contains(text() , 'Add Preventive Action')]"
    QI_Validation_Notrequired_WebElement_xpath="//div[@id='validationPhase']//div[@class='media-body']"
    QI_CloseQI_Reason_WebEdit_xpath="//div[@class='modal-body']//div//textarea"
    QI_CloseQI_Status_xpath="//div[@class='col-12 action-header media']//div[2]"
    QI_Complete_QI_button_xpath="//button[@class='success margin-right-small']"
    QI_Cancel_QI_button_xpath="//button[@class='danger margin-right-small']"
    QI_Actions_WebElement_xpath="//li[@class='active']"

# Time Line Xpaths
    QI_TimeLine_QIcreated_WebElement_xpath="(//ul[@class='timeline-vertical']//li[@class='media'])[1]"
    QI_TimeLine_Containmentstarted_WebElement_xpath ="(//ul[@class='timeline-vertical']//li[@class='media'])[2]"












# QI Home page
#     QI_Filter_Status_SelectBox_xpath="//td[3]//select[1]"
#     QI_Filter_JNPROwner_WebEdit_xpath="//td[5]//input[1]"
#     QI_Filter_Apply_WebElement_xpath="//button[@class='margin-right']"
#     QI_Existing_QIID_WebElement_xpath=" //section[3]//div[1]//table[1]//tbody[1]//tr[1]//td[1]"
    #QI_Verify_Affected_Section_check_xpath="//button[@name='qiAffectedItemsbutton']//i[@class='icon icon-check-circle text-color-green']"



