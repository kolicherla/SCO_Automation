from QA.PageObjects.Test_Locators import QET
from QA.Utilities.PerformAction import PerformActions
from QA.Utilities.CommonLib import CommonFunctions
import time

class EditQIPs():
    global objCommon, objActions
    objCommon = CommonFunctions()
    objActions = PerformActions()


# Editing the QIP
    def EditQIP(self, UpdatedProblemDescription, JuniperWatchList, SupplierQIPteam, JuniperQIPTeam, SupplierWatchList):
        strProblemDescription = objActions.getText(QET.Description_WebElement_xpath, "xpath")
        # print("Text in problem Description field:" + strProblemDescription)
        objActions.clickElement(QET.EditQIP_button_xpath, "xpath")
        time.sleep(2)
        objActions.enterText(QET.JuniperWatchList_WebEdit_xpath, "xpath", JuniperWatchList)
        objActions.selectDropdown(QET.Supplier_QIPteam_Selectbox_xpath, "xpath", "visibletext", SupplierQIPteam )
        time.sleep(2)
        objActions.enterText(QET.Juniper_QIPTeam_WebEdit_xpath, "xpath", JuniperQIPTeam)
        objActions.selectDropdown(QET.SupplierWatchList_WebEdit_xpath, "xpath", "visibletext", SupplierWatchList )
        objActions.enterText(QET.ProblemDescription_WebEdit_xpath, "xpath", UpdatedProblemDescription)
        objActions.clickElement(QET.Save_button_xpath, "xpath")
        time.sleep(2)
        strUpdatedPD = objActions.getText(QET.Description_WebElement_xpath, "xpath")
        print("Text in Updated problem Description field:" +strUpdatedPD)
        objCommon.capture_screenshot("QIP Edited Successfully")
        time.sleep(2)
        if strProblemDescription != strUpdatedPD:
            print("Successfully edited QIP")
        else:
            print("Unable to edit the QIP")
            assert strProblemDescription != strUpdatedPD