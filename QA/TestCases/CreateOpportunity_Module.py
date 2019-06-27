from QA.PageObjects.Opportunities_Page import opportunity_Page
from QA.Utilities.CommonLib import CommonFunctions
from QA.PageObjects.Login_Page import login_Page
import time

class Test_Opportunity():
    global objCommonLib
    objCommonLib = CommonFunctions()

    def test_TC001_SCAR_CreateOpportunity(self,setup,TestData):
        objlogin=login_Page()
        objlogin.QET_Login(TestData['UserName'],TestData['Password'])
        objCommonLib.capture_screenshot('Login Page')
        time.sleep(5)
        objOpp=opportunity_Page()
        objOpp.CreateOpportunity(TestData['NewSupplier'],TestData['NewMPin'],TestData['SupplierPCN'])
        objCommonLib.capture_screenshot('Logged out')
