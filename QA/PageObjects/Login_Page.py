from QA.Base.Config import MyConfigFiles
from QA.Locators.Test_Locators import MyJuniperLocators
from selenium import webdriver

class login_Page():

    def QET_Login(self,UserName,Password):
        MyConfigFiles.driver.find_element_by_id(MyJuniperLocators.username_textbox_id).send_keys(UserName)
        MyConfigFiles.driver.find_element_by_id(MyJuniperLocators.password_textbox_id).send_keys(Password)
        MyConfigFiles.driver.find_element_by_xpath(MyJuniperLocators.submit_button_xpath).click()



