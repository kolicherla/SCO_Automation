from QA.PageObjects.Test_Locators import QET
from QA.Utilities.PerformAction import PerformActions
from QA.Utilities.CommonLib import CommonFunctions
from QA.Base.Config import MyConfigFiles
import time

class Home():
    global objCommon, objActions, objConfig
    objCommon = CommonFunctions()
    objActions = PerformActions()
    objConfig=MyConfigFiles()

    def ClickSCARButton(self):
        objActions.clickElement(QET.SCARs_link_xpath, "xpath")
        objCommon.capture_screenshot('Clicked on SCAR Link')

    def ClickQIPButton(self):
        objActions.clickElement(QET.QIPs_link_xpath, "xpath")
        objCommon.capture_screenshot('Clicked on QIP Link')

    def ClickQIButton(self):
        objActions.clickElement(QET.QIs_link_xpath, "xpath")
        objCommon.capture_screenshot('Clicked on QIs Link')