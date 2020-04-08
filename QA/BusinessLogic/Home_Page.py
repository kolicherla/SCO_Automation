from QA.PageObjects.Test_Locators import PCN
from QA.Utilities.PerformAction import PerformActions
from QA.Utilities.CommonLib import CommonFunctions
from QA.Base.Config import MyConfigFiles
import time

class Home():
    global objCommon, objActions, objConfig
    objCommon = CommonFunctions()
    objActions = PerformActions()
    objConfig=MyConfigFiles()

    def ClickSwitchRolesLnk(self):
        objActions.clickElement(PCN.Switch_Roles_link_xpath, "xpath")

    def DashboardLnk(self):
        objActions.clickElement(PCN.DashBoard_Button_xpath,"xpath")

    def ClickAdminlnk(self):
        objActions.clickElement(PCN.Admin_link_xpath, "xpath")


    def ClickReportsLnk(self):
        objActions.clickElement(PCN.Reports_link_xpath, "xpath")


    def ClickSearchLnk(self):
        objActions.clickElement(PCN.Search_link_xpath, "xpath")


    # def SelectContextCE(self):
    #     objActions.clickElement(PCN.ContextCE_WebElement_xpath, "xpath")
    #     objCommon.capture_screenshot('Selected Context CE radio button')
    #
    # def SelectGlobalCM(self):
    #     objActions.clickElement(PCN.Global_CM_WebElement_xpath, "xpath")
    #     objCommon.capture_screenshot('Selected Global Commodity Manager radio button')
    #
    # def SelectNPIMaterialPM(self):
    #     objActions.clickElement(PCN.NPI_Material_PM_WebElement_xpath, "xpath")
    #     objCommon.capture_screenshot('Selected NPI Material PM button')
    #
    # def SelectNPIMPM(self):
    #     objActions.clickElement(PCN.NPI_MPM_WebElement_xpath, "xpath")
    #     objCommon.capture_screenshot('Selected NPI MPM button')
