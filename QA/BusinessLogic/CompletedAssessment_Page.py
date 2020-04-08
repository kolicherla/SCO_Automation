from QA.Utilities.PerformAction import PerformActions
from QA.PageObjects.Test_Locators import PCN
from QA.Utilities.CommonLib import CommonFunctions
from QA.Base.Config import MyConfigFiles
from QA.BusinessLogic.Home_Page import Home
from QA.BusinessLogic.Filter_Page import Filter
from QA.BusinessLogic.CreateJPCN_Page import createJPCN_Page
from QA.BusinessLogic.JPCNStatusOverview_Page import JPCNstatusoverview_Page
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
from pathlib import Path
from selenium import webdriver
import sys
import datetime
from pytz import timezone
import time

class CompleteAssessment_Page():
    global objCommon, objActions ,objConfig,objFilter,objHome,objCreateJPCN,objJPCNStatusOverview
    objCommon = CommonFunctions()
    objActions = PerformActions()
    objConfig=MyConfigFiles()
    objFilter=Filter()
    objHome=Home()
    objCreateJPCN = createJPCN_Page()
    objJPCNStatusOverview=JPCNstatusoverview_Page()



    def Verify_CompleteAssessment(self,strJPNID):
        time.sleep(2)
        objActions.clickElement(PCN.DashBoard_ContextCE_CompleteAssessment_WebElement_xapth, "xpath")
        objJPCNStatusOverview.SelectJCPN(strJPNID)
        objCommon.capture_screenshot("Completed Assessment page display")
        strPageHeader=objActions.getText(PCN.Completed_Assessement_PageHeader_WebElement_xpath, "xpath")
        assert (objActions.getText(PCN.Completed_Assessement_PageHeader_WebElement_xpath, "xpath"))
        print("Completed Assessment page displayed Sucessfully:"  +strPageHeader )






