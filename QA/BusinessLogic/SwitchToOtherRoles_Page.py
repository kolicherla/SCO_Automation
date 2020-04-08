from QA.PageObjects.Test_Locators import PCN
from QA.Utilities.PerformAction import PerformActions
from QA.Utilities.CommonLib import CommonFunctions
from QA.Base.Config import MyConfigFiles
from QA.BusinessLogic.Home_Page import Home
from QA.BusinessLogic.Filter_Page import Filter
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from pathlib import Path

import time

class SwitchToRoles_Page():
    global objCommon, objActions, objConfig,objHome,objFilter
    objCommon = CommonFunctions()
    objActions = PerformActions()
    objConfig=MyConfigFiles()
    objFilter=Filter()
    objHome=Home()

#Role Types Available[Context CE, Global Commodity Manager, NPI Material PM, NPI MPM]
    def SwitchToRole(self,roleType):
        time.sleep(3)
        objHome.ClickSwitchRolesLnk()
        time.sleep(2)
        objActions.clickElement(PCN.Submit_SR_button_xpath, "xpath")
        objActions.clickElement("//span[text()='"+roleType+"']/input","xpath")
        print("Sucessfully selected the role: "+roleType)
        objCommon.capture_screenshot("Role Selected")
        objActions.clickElement(PCN.Submit_SR_button_xpath, "xpath")