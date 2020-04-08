from QA.PageObjects.Test_Locators import PCN
from QA.Utilities.PerformAction import PerformActions
from QA.Utilities.CommonLib import CommonFunctions

class login_Page():
    global objCommon,objActions, objPCN
    objCommon=CommonFunctions()
    objActions = PerformActions()

    def PCN_Login(self,UserName,Password):
        objActions.enterText(PCN.username_textbox_id,"id",UserName)
        objActions.enterText(PCN.password_textbox_id,"id",Password)
        objActions.clickElement(PCN.submit_button_xpath,"xpath")
        objCommon.capture_screenshot('Login Page Successfull')

    def PCN_LogOut(self):
        objActions.clickElement(PCN.logout_link_xpath,"xpath")





