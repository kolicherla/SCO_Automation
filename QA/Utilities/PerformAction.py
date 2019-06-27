from QA.Locators.Test_Locators import MyJuniperLocators
from QA.Base.Config import MyConfigFiles
import time
import sys
import os
from selenium.webdriver.support.ui import Select

class PerformActions():
    def clickLink(objlocators, msg ):
        try:
            centerText = MyConfigFiles.driver.find_element_by_xpath (objlocators).click()
            print ( "Success:: Verify to click on the link" , msg)
        except:
            print("Failed:: Not clicked on the link ", msg)
        time.sleep ( 2 )
        return centerText

    def enterText(objLocators, TextToEnter,  msg):
        try:
            MyConfigFiles.driver.find_element_by_xpath(objLocators).send_keys(TextToEnter)
            print("Success:: Verify to enter the text", msg)
        except:
            print("Failed:: Not entered the text ", msg)

    def clickButton(objLocators, msg ):
        try:
            MyConfigFiles.driver.find_element_by_xpath(objLocators).click()
            print ("Success:: Verify to click on button", msg)
        except:
            print("Failed:: Verified to click on button ", msg)

    def selectDropdown(objLocators, msg ):
        try:
            selectDropDownValues=Select(MyConfigFiles.driver.find_element_by_xpath(objLocators))
            selectDropDownValues.select_by_index(1)
            print ( "Success:: Verify to select the drop down values", msg)
        except:
            print ( "Failed:: Verify to select the drop down values", msg)

    def getFunctionName(self):
        try:
            this_function_name = sys._getframe(2).f_code.co_name
            return this_function_name
        except:
            print("Failed:: Verify to get the parent function name")

    def getCurrentDirectory(self):
        try:
            this_current_dir = os.getcwd()
            return this_current_dir
        except:
            print(" Failed:: Verify to get the current directory")

    def createdirectory(WorkingDirectory):
        if not os.path.exists(WorkingDirectory):
            os.makedirs(WorkingDirectory)
            #print("Directory ", WorkingDirectory, " Created ")
        else:
            pass
            #print("Directory ", WorkingDirectory, " already exists")