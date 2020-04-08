from QA.PageObjects.Test_Locators import PCN
from QA.Utilities.PerformAction import PerformActions
from QA.Utilities.CommonLib import CommonFunctions
from QA.Base.Config import MyConfigFiles
import time

class Filter():
    global objCommon, objActions, objConfig
    objCommon = CommonFunctions()
    objActions = PerformActions()
    objConfig=MyConfigFiles()

    def ClickCreate(self):
        objActions.clickElement(QET.Create_button_xpath, "xpath")

# Method to navigate to the screen from login page
    def NavigateToSCAR(self, ScarID):
        objActions.clickElement(QET.SCARs_link_xpath, "xpath")
        objActions.clickElement("//a[text()='" + ScarID + "']", "xpath")
        time.sleep(2)

# Method to navigate to the screen from login page
    def NavigateToQIP(self, QIPID):
        objActions.clickElement(QET.QIPs_link_xpath, "xpath")
        objActions.clickElement("//a[text()='" + QIPID + "']", "xpath")
        time.sleep(2)


# Method to navigate to the screen from login page
    def NavigateToQI(self, QIID):
        objActions.clickElement(QET.QIs_link_xpath, "xpath")
        objActions.clickElement("//a[text()='" + QIID + "']", "xpath")
        time.sleep(2)

