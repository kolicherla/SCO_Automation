from QA.PageObjects.Test_Locators import QET
from QA.Utilities.PerformAction import PerformActions
from QA.Utilities.CommonLib import CommonFunctions
import time

class EditSCARs():
    global objCommon, objActions
    objCommon = CommonFunctions()
    objActions = PerformActions()

    # Editing the SCAR
    def EditSCAR(self, UpdatedProblemDescription):
        strProblemDescription = objActions.getText(QET.Description_WebElement_xpath, "xpath")
        # print("Text in problem Description field:" + strProblemDescription)
        objActions.clickElement(QET.EditSCAR_button_xpath, "xpath")
        time.sleep(2)
        objActions.enterText(QET.ProblemDescription_WebEdit_xpath, "xpath", UpdatedProblemDescription)
        objActions.clickElement(QET.Save_button_xpath, "xpath")
        time.sleep(2)
        strUpdatedPD = objActions.getText(QET.Description_WebElement_xpath, "xpath")
        # print("Text in Updated problem Description field:" +strUpdatedPD)
        objCommon.capture_screenshot("SCAR Edited Successfully")
        if strProblemDescription != strUpdatedPD:
            print("Successfully updated the problem description from "+strProblemDescription + " to "+strUpdatedPD)
        else:
            print("Could not update the problem description from "+strProblemDescription + " to "+UpdatedProblemDescription)
        assert strProblemDescription != strUpdatedPD