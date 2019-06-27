from QA.Locators.Test_Locators import MyJuniperLocators
from QA.Base.Config import MyConfigFiles
import time
class opportunity_Page():

    def verify_QualTracker(self):
        MyConfigFiles.driver.find_element_by_link_text(MyJuniperLocators.QualTracker_link_linktext)

    def CreateOpportunity(self,NewSupplier,NewMPin,SupplierPCN):
        MyConfigFiles.driver.find_element_by_xpath(MyJuniperLocators.createOpportunity_btn_xpath).click()
        MyConfigFiles.driver.find_element_by_xpath(MyJuniperLocators.pcndesign_button_xpath).click()
        MyConfigFiles.driver.find_element_by_xpath(MyJuniperLocators.NewSupplier_webedit_xpath).send_keys(NewSupplier)
        MyConfigFiles.driver.find_element_by_xpath(MyJuniperLocators.NewMPin_webedit_xpath).send_keys(NewMPin)
        MyConfigFiles.driver.find_element_by_xpath(MyJuniperLocators.SupplierPCN_webedit_xpath).send_keys(SupplierPCN)
        time.sleep(3)
        MyConfigFiles.driver.find_element_by_xpath(MyJuniperLocators.Cancel_btn_xpath).click()

