from selenium import webdriver
import pytest
import time
from selenium.webdriver.support.ui import Select
from QA.Locators.Test_Locators import MyJuniperLocators
from QA.Base.Config import MyConfigFiles

class TestMyJuniperLandingClass():
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_01_VerifyToOpenmyJuniperBrowser(self, setup):
        time.sleep(2)
        try:
            eleExists=MyConfigFiles.driver.find_element_by_xpath(MyJuniperLocators.landingPage_Logo_xPath).is_displayed()
            if (eleExists == True):
                print("Success::MyJuniper page Presents and it displays MyJuniper Icon", "MyJuniper Logo exists: ", eleExists)
            else:
                print("Failed: MyJuniper page not present and it not displays MyJuniper Icon")
        except:
            print("Failed: MyJuniper page not present and it not displays MyJuniper Icon")

    @pytest.mark.regression
    def test_02_VerifyMyJuniperTitle(self, setup):
        time.sleep(2)
        assert "Login : Juniper Networks" in MyConfigFiles.driver.title
        print ( "Success:: Verify title of the My Juniper page" )

    @pytest.mark.regression
    def test_03_VerifyCreateNewAccountLink(self, setup):
        time.sleep(2)
        print("Success:: Verify the link of the New Account creation option")
        centerText = MyConfigFiles.driver.find_element_by_xpath(MyJuniperLocators.create_New_Account_xPath).text
        assert "Create a New Account" == centerText
        time.sleep ( 2 )

    @pytest.mark.regression
    def test_04_VerifyLandonToAccountSetupPage(self, setup):
        centerText = MyConfigFiles.driver.find_element_by_xpath(MyJuniperLocators.create_New_Account_xPath).click()
        time.sleep ( 2 )
        print ( "Success:: Verify to click on the New Account link and reached to Account SetUp Page" )
        assert "Create User Account - Juniper Networks Account Management" in MyConfigFiles.driver.title