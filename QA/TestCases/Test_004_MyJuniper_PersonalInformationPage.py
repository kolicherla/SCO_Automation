from selenium import webdriver
import pytest
import time
from QA.Locators.Test_Locators import MyJuniperLocators
from QA.Base.Config import MyConfigFiles

class TestHTMLReport():
    def test_homepageTitle(self,setup):

        print("Success:: Verify the link of the New Account creation option")
        time.sleep(2)
        assert MyConfigFiles.driver.title=="Login : Juniper Networks"

    def test_03_VerifyCreateNewAccountLink(self, setup):
        time.sleep(2)
        print("Success:: Verify the link of the New Account creation option")
        centerText = MyConfigFiles.driver.find_element_by_xpath(MyJuniperLocators.create_New_Account_xPath).text
        assert "Create a New Account" == centerText