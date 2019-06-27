from QA.PageObjects.Login_Page import login_Page
from QA.Base.Config import MyConfigFiles
from QA.PageObjects.Opportunities_Page import opportunity_Page
from QA.Utilities.CommonLib import CommonFunctions
import time
import pytest

class Test_QETLogin_Application():
    global objCommonLib
    objCommonLib=CommonFunctions()

    def test_TC001_SCAR_LoginValidCredentials(self,setup,TestData):
        login=login_Page()
        objCommonLib.capture_screenshot('Login page')
        login.QET_Login(TestData['UserName'],TestData['Password'])
        time.sleep(5)
        strTitle=MyConfigFiles.driver.title
        objCommonLib.capture_screenshot('Login successfull')
        assert "Qualification Tracker: Juniper Networks" in strTitle

    def test_TC002_QIP_CreateOpportunity(self,setup,TestData):
        objlogin=login_Page()
        objCommonLib.capture_screenshot("Login Page")
        objlogin.QET_Login(TestData['UserName'],TestData['Password'])
        time.sleep(5)
        objOpp=opportunity_Page()
        objCommonLib.capture_screenshot("Create Opportunity")
        objOpp.CreateOpportunity(TestData['NewSupplier'],TestData['NewMPin'],TestData['SupplierPCN'])






