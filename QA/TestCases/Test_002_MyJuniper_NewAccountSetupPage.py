import time
import pytest
from QA.Locators.Test_Locators import MyJuniperLocators
from QA.Base.Config import MyConfigFiles
from QA.Utilities.PerformAction import PerformActions

class TestMyJuniperNewAccountClass():
    def test_02_VerifyUserRegisterationSetupPage (self, setup ):
        PerformActions.clickLink(MyJuniperLocators.create_New_Account_xPath, "New User Account at Juniper Landing Page")
        assert "Create User Account - Juniper Networks Account Management" in MyConfigFiles.driver.title
        print ("Success:: Verify to Land on to Registeration SetUp Page")

        PerformActions.enterText(MyJuniperLocators.newUser_eMail_xPath,"testone@in.com","New User eMail at Juniper new account setup page")
        PerformActions.enterText(MyJuniperLocators.reEnterNewUser_eMail_xPath,"testone@in.com","New User Reenter eMail at Juniper new account setup page")

        PerformActions.selectDropdown(MyJuniperLocators.countryDropDown_xPath," from country at New user Account setup page")

        PerformActions.clickButton(MyJuniperLocators.clickNextBtn_xPath, "Next> in New User Account Setup Page")

        time.sleep ( 2 )
        assert "Registration Details - Juniper Networks Account Management" in MyConfigFiles.driver.title
        print ("Success:: Verify to reach User Registration page")