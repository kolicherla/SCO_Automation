from QA.PageObjects.Test_Locators import PCN
from QA.Utilities.PerformAction import PerformActions
from QA.Utilities.CommonLib import CommonFunctions
from QA.Base.Config import MyConfigFiles
from QA.BusinessLogic.Home_Page import Home
from QA.BusinessLogic.Filter_Page import Filter
from QA.BusinessLogic.CreateJPCN_Page import createJPCN_Page
from QA.BusinessLogic.JPCNStatusOverview_Page import JPCNstatusoverview_Page
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from pathlib import Path
import sys
import time

class InitilaAssessment_Page():
    global objCommon, objActions, objConfig,objHome,objFilter,objCreateJPCN,objJPCNStatusOverview
    objCommon = CommonFunctions()
    objActions = PerformActions()
    objConfig=MyConfigFiles()
    objFilter=Filter()
    objHome=Home()
    objCreateJPCN = createJPCN_Page()
    objJPCNStatusOverview = JPCNstatusoverview_Page()


    def InitialAssessment_ContextCE_Details(self,CCER,priorityType,PCNTYPE,ASQNeeded):
        time.sleep(3)
        objActions.selectDropdown(PCN.ContextCE_Recommendation_SelectBox_name, "name", "visibletext", CCER)
        time.sleep(3)
        ContextCE_RC=objCreateJPCN.GenerateRandominteger()
        objActions.enterText(PCN.ContextCE_RecommendationComments_WebEdit_name, "name", ContextCE_RC)
        objActions.selectDropdown(PCN.Priority_Type_selectBox_name, "name", "visibletext", priorityType)
        time.sleep(2)
        if PCNTYPE == 'EOL':
           time.sleep(2)
           objActions.selectDropdown(PCN.IA_Alternative_SourceQN_SelectBox_name, "name", "visibletext", ASQNeeded)
           time.sleep(2)
           ASQNComments=objCreateJPCN.GenerateRandominteger()
           objActions.enterText(PCN.IA_FFF_Alternative_SourceComments_WedEdit_name, "name", ASQNComments)

    def InitialAssessment_AddNewRecord(self,DeviationStatus,MCOECO):
        objActions.clickElement(PCN.IA_AddNewRecord_WebElement_xpath, "xpath")
        time.sleep(2)
        PR=objCreateJPCN.GenerateRandominteger()
        objActions.enterText(PCN.AddNewRecord_PR_WebEdit_name, "name", PR)
        Deviation = objCreateJPCN.GenerateRandominteger()
        objActions.enterText(PCN.AddNewReocrd_Deviation_WebEdit_name, "name", Deviation)
        objActions.selectDropdown(PCN.AddNewRecord_DeviationStatus_selectBox_name, "name", "visibletext",  DeviationStatus)
        time.sleep(3)
        Seventeneleveen = objCreateJPCN.GenerateRandominteger()
        objActions.enterText(PCN.AddNewRecord_710_711_WebEdit_name, "name", Seventeneleveen)
        JPN = objCreateJPCN.GenerateRandominteger()
        objActions.enterText(PCN.AddNewRecord_JPN_WebEdit_name, "name", JPN)
        MPN = objCreateJPCN.GenerateRandominteger()
        objActions.enterText(PCN.AddNewRecord_MPN_WebEdit_name, "name", MPN)
        HTR = objCreateJPCN.GenerateRandominteger()
        objActions.enterText(PCN.AddNewRecord_HTR_WebEdit_name, "name", HTR)
        time.sleep(2)
        objActions.enterText(PCN.AddNewRecord_ECOMCO_WebEdit_name, "name", MCOECO)
        QPET = objCreateJPCN.GenerateRandominteger()
        objActions.enterText(PCN.AddNewRecord_qpet_WebEdit_name, "name", QPET)
        time.sleep(2)
        Comments = objCreateJPCN.GenerateRandominteger()
        objActions.enterText(PCN.AddNewRecord_Comment_WebEdit_name, "name", Comments)
        JuniperAssembly = objCreateJPCN.GenerateRandominteger()
        objActions.enterText(PCN.AddNewRecord_JA_WebEdit_name, "name", JuniperAssembly)
        time.sleep(3)
        objActions.clickElement(PCN.AddNewAttachement_SubmitBtn_xpath, "xpath")


    def QualDataReview_Attachement(self,strFilePath,QualReportStatus):
        time.sleep(2)
        objCommon.AttachFile(strFilePath, PCN.QualDataReview_Attachement_xpath, "xpath")
        objActions.clickElement(PCN.QualDataReview_Upload_xpath, "xpath")
        time.sleep(3)
        objActions.selectDropdown(PCN.QualReport_AcceptStaus_name, "name", "visibletext", QualReportStatus)
        time.sleep(3)
        QualReportComments=objCreateJPCN.GenerateRandominteger()
        objActions.enterText(PCN.QualReport_ReviewComments_name, "name", QualReportComments)
        time.sleep(2)

    def Complete_Assessment(self):
        time.sleep(2)
        objActions.clickElement(PCN.Complete_Assessment_Button_xpath, "xpath")
        time.sleep(2)

    def Submit_OnWarringWindow(self):
        time.sleep(4)
        objActions.clickElement(PCN.submit_button_xpath, "xpath")
        time.sleep(2)


    def Verify_GCM_DashBoard(self,strJPNID):
        time.sleep(2)
        GCM_COunt=int(objActions.getText(PCN.DashBoard_GCMAssessment_Count_xpath, "xpath"))
        if GCM_COunt == 0:
            objCommon.capture_screenshot("Update JPCN information not displayed in the GCM assessment")
            print("Create JPCN is not displayed in the GCM Dashboard")
        else:
            objActions.clickElement(PCN.DashBoard_GCMAssessment_WebElement_xpath, "xpath")
            objCommon.capture_screenshot("GCM Assessment JPCN Status Overview")
            objJPCNStatusOverview.Compare_GCM_JPCN(strJPNID)




        # strGCM = objActions.getText(PCN.GCM_Button_WebElement_xpath, "xpath")
        # print("GCM Table is displayed in the Initial Assessment page:" +strGCM)
        # objCommon.capture_screenshot("GCM Table")
        # time.sleep(2)
        #
        #
        # time.sleep(2)




    def InitialAssessment_Checking_AutoPopulationOfPCNCompliance(self,PCNTYPE,intEFRCDiff,intBRDiff,intSBDiff,ReasonforNC):
        time.sleep(2)
        objActions.ValidationOnSelectedtext(PCN.IA_PCNCompliance_SelectBox_name, "name")
        if PCNTYPE =="Process Change" or PCNTYPE=="Design Change":
            strPCNComplience = objActions.ValidationOnSelectedtext(PCN.IA_PCNCompliance_SelectBox_name, "name")
            if intEFRCDiff >= 90:
                if strPCNComplience == "Compliant":
                    print("Where:" +PCNTYPE+ "and Effective and Received date >=90 then PCN Compliance is Autopopulates to :" " "+strPCNComplience)
                    objCommon.capture_screenshot("PCN Compliance as: Compliant ")
                else:
                    print("PCNComplience dropdown displaying as :" " " +strPCNComplience+ "insted of : Compliant")
                    assert strPCNComplience == "Compliant"
            elif intEFRCDiff < 90:
                 if strPCNComplience == "Non-Compliant":
                    time.sleep(2)
                    objActions.selectDropdown(PCN.Reasonfor_NonCompliance_SelectBox_name, "name", "visibletext", ReasonforNC)
                    time.sleep(2)
                    print("Where:" +PCNTYPE+ "and Effective and Received date < 90 then PCN Compliance is Autopopulates to :" " "+strPCNComplience)
                    objCommon.capture_screenshot("PCN Compliance as: Non-Compliant ")
                 else:
                    print("PCNComplience dropdown displaying as :" " " +strPCNComplience+ "insted of: Non-Compliant ")
                    assert strPCNComplience == "Non-Compliant"
        elif PCNTYPE == "EOL":
             strPCNComplience = objActions.ValidationOnSelectedtext(PCN.IA_PCNCompliance_SelectBox_name, "name")
             if intBRDiff >= 180:
                 if strPCNComplience == "Compliant":
                     print("Where:" + PCNTYPE + "and Effective and Received date >=180 then PCN Compliance is Autopopulates to :" " " + strPCNComplience)
                     objCommon.capture_screenshot("PCN Compliance as: Compliant ")
                 else:
                     print("PCNComplience dropdown displaying as :" " " + strPCNComplience + "insted of : Compliant")
                     assert strPCNComplience == "Compliant"
             elif intBRDiff < 180:
                  if strPCNComplience == "Non-Compliant":
                      time.sleep(2)
                      objActions.selectDropdown(PCN.Reasonfor_NonCompliance_SelectBox_name, "name", "visibletext",  ReasonforNC)
                      time.sleep(2)
                      print("Where:" + PCNTYPE + "and Effective and Received date < 180 then PCN Compliance is Autopopulates to :" " " + strPCNComplience)
                      objCommon.capture_screenshot("PCN Compliance as: Non-Compliant ")
                  else:
                      print("PCNComplience dropdown displaying as :" " " + strPCNComplience + "insted of: Non-Compliant ")
                      assert strPCNComplience == "Non-Compliant"
             elif intSBDiff >= 180:
                 if strPCNComplience == "Compliant":
                     print("Where:" + PCNTYPE + "and Effective and Received date >=180 then PCN Compliance is Autopopulates to :" " " + strPCNComplience)
                     objCommon.capture_screenshot("PCN Compliance as: Compliant ")
                 else:
                     print("PCNComplience dropdown displaying as :" " " + strPCNComplience + "insted of : Compliant")
                     assert strPCNComplience == "Compliant"
             elif intSBDiff < 180:
                  if strPCNComplience == "Non-Compliant":
                      time.sleep(2)
                      objActions.selectDropdown(PCN.Reasonfor_NonCompliance_SelectBox_name, "name", "visibletext", ReasonforNC)
                      time.sleep(2)
                      print("Where:" + PCNTYPE + "and Effective and Received date < 180 then PCN Compliance is Autopopulates to :" " " + strPCNComplience)
                      objCommon.capture_screenshot("PCN Compliance as: Non-Compliant ")
                  else:
                      print("PCNComplience dropdown displaying as :" " " + strPCNComplience + "insted of: Non-Compliant ")
                      assert strPCNComplience == "Non-Compliant"
        else:
            print("Failed: PCN Compliance not displaying Expected values  and  conditions are not satisfied")
            objCommon.capture_screenshot("No Such element found")
















