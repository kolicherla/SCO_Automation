from QA.PageObjects.Test_Locators import QET
from QA.Utilities.PerformAction import PerformActions
from QA.Utilities.CommonLib import CommonFunctions

class login_Page():
    global objCommon,objActions, objScar
    objCommon=CommonFunctions()
    objActions = PerformActions()

    def QET_Login(self,UserName,Password):
        objActions.enterText(QET.username_textbox_id,"id",UserName)
        objActions.enterText(QET.password_textbox_id,"id",Password)
        objActions.clickElement(QET.submit_button_xpath,"xpath")
        objCommon.capture_screenshot('Login Page Successfull')

    def QET_LogOut(self):
        objActions.clickElement(QET.logout_link_xpath,"xpath")





