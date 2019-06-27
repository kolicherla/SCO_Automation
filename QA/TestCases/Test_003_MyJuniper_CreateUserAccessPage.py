from selenium import webdriver
import pytest
import time
from selenium.webdriver.support.ui import Select
from QA.Locators.Test_Locators import MyJuniperLocators
from QA.Base.Config import MyConfigFiles
from QA.Utilities.PerformAction import PerformActions

class TestMyJuniperCreateUserAccess():

    def test_03_VerifyToCreateUserAccountPage (self, setup ):
        PerformActions.clickLink ( MyJuniperLocators.create_New_Account_xPath,"New User Account at Juniper Landing Page" )

        PerformActions.enterText(MyJuniperLocators.newUser_eMail_xPath,"testone@in.com","New User eMail at Juniper new account setup page")
        PerformActions.enterText(MyJuniperLocators.reEnterNewUser_eMail_xPath,"testone@in.com","New User Reenter eMail at Juniper new account setup page")

        PerformActions.selectDropdown(MyJuniperLocators.countryDropDown_xPath," from country at New user Account setup page")

        PerformActions.clickButton(MyJuniperLocators.clickNextBtn_xPath, "Next> in New User Account Setup Page")

        guestUserText = MyConfigFiles.driver.find_element_by_xpath ("//label[contains(text(),'Guest User Access')]" ).text
        assert "Guest User Access" == guestUserText
        print ( "Success:: Verify guest User Access radio button getting displayed in user registeration page" )
        try :
            MyConfigFiles.driver.find_element_by_xpath ( "//input[@id='guest']" ).click ()
            print ( "Passed:: Verify on selection of Access User Radio button in user registration page" );
        except :
            print ( "Failed:: Verify on selection of Access User Radio button in user registration page" );
        time.sleep ( 2 )
        try :
            MyConfigFiles.driver.find_element_by_xpath ( "//input[@type='checkbox']" ).click ()
            print ( "Passed:: Verify on selection of check box since user selected as Guest" );
        except :
            print ( "Failed:: Verify on selection of checkbox since user selected as Guest" );
        try :
            MyConfigFiles.driver.find_element_by_xpath ( "//input[@value='Next>']" ).click ()
            print ( "Passed:: Verify on click on Next> button in User Registration" );
        except :
            print ( "Failed:: Verify on click on Next> button in User Registration" );
        time.sleep ( 2 )
        try :
            UserRegistrationText = MyConfigFiles.driver.find_element_by_xpath ( "//div[@class='heroContentShort']/h1" ).text
            assert "USER REGISTRATION" == UserRegistrationText
            print ( "Success:: Verify to successful land on to Account Creation page", UserRegistrationText,
                    "::User Registration Text" )
        except :
            print ( "Failed:: Verify to successful land on to Account Creation page", UserRegistrationText,
                    "::User Registration Text" )