from QA.Base.Config import MyConfigFiles
from QA.Locators.Test_Locators import MyJuniperLocators
import time
from selenium.webdriver.support.ui import Select

class createSCAR_Page():

    def CreateSCAR(self,ProblemDescription,AffectedPart,UserGroup,Supplier,Contact,Escalation,Jn_Escalation):
        #click on SCAR Link
        MyConfigFiles.driver.find_element_by_xpath(MyJuniperLocators.SCARs_link_xpath).click()
        time.sleep(2)
        MyConfigFiles.driver.find_element_by_xpath(MyJuniperLocators.Create_button_xpath).click()
        MyConfigFiles.driver.find_element_by_xpath(MyJuniperLocators.ProblemDescription_WebEdit_xpath).send_keys(ProblemDescription)
        MyConfigFiles.driver.find_element_by_xpath(MyJuniperLocators.AffectedPart_webEdit_xpath).click()
        time.sleep(2)
        MyConfigFiles.driver.find_element_by_xpath("//li[@data-part='" + AffectedPart + "']").click()
        objUserGroup=Select(MyConfigFiles.driver.find_element_by_xpath(MyJuniperLocators.UserGroup_SelectBox_xpath))
        objUserGroup.select_by_value(UserGroup)
        time.sleep(2)
        objSupplier=Select(MyConfigFiles.driver.find_element_by_xpath(MyJuniperLocators.Supplier_SelectBox_xpath))
        objSupplier.select_by_visible_text(Supplier)
        objContact=Select(MyConfigFiles.driver.find_element_by_xpath(MyJuniperLocators.Contact_SelectBox_xpath))
        objContact.select_by_visible_text(Contact)
        objEscalation = Select(MyConfigFiles.driver.find_element_by_xpath(MyJuniperLocators.Escalation_SelectBox_xpath))
        objEscalation.select_by_visible_text(Escalation)
        MyConfigFiles.driver.find_element_by_xpath(MyJuniperLocators.Escalation_WebEdit_xpath).send_keys(Jn_Escalation)
        time.sleep(2)
        MyConfigFiles.driver.find_element_by_xpath("//span[text()='" + Jn_Escalation + "']").click()    #dynamic value
        time.sleep(2)
        objJnWatchlist=MyConfigFiles.driver.find_element_by_xpath(MyJuniperLocators.SupplierWatchList_WebEdit_xpath)
        objJnWatchlist.select_by_index(5)
        MyConfigFiles.driver.find_element_by_xpath(MyJuniperLocators.CreateScar_button_xpath).click()

