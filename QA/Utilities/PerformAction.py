from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from QA.Base.Config import MyConfigFiles
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import QA.Utilities.CommonLib as CL
import sys
import os

class PerformActions():

##Method to click on a WebElement(Button, Image, Webelement, link)
# Parameters
# locatorType: Name of the locator used
# locator: Value of the locator
    def clickElement(self,locator,locatorType):
        CL.CommonFunctions.presenceOfElement(self,locator,locatorType)
        try:
            if locatorType.upper() == "XPATH":
                objElement = WebDriverWait(MyConfigFiles.driver, MyConfigFiles.Implicit_Time_Out).until(
                    EC.element_to_be_clickable((By.XPATH, locator)))
                objElement.click()
            elif locatorType.upper() == "ID":
                objElement=WebDriverWait(MyConfigFiles.driver, MyConfigFiles.Implicit_Time_Out).until(
                    EC.element_to_be_clickable((By.ID, locator)))
                objElement.click()
            elif locatorType.upper() == "NAME":
                objElement = WebDriverWait(MyConfigFiles.driver, MyConfigFiles.Implicit_Time_Out).until(
                    EC.element_to_be_clickable((By.NAME, locator)))
                objElement.click()
            elif locatorType.upper() == "lINKTEXT":
                objElement = WebDriverWait(MyConfigFiles.driver, MyConfigFiles.Implicit_Time_Out).until(
                    EC.element_to_be_clickable((By.LINK_TEXT, locator)))
                objElement.click()
            elif locatorType.upper() == "PARTIALLINKTEXT":
                objElement = WebDriverWait(MyConfigFiles.driver, MyConfigFiles.Implicit_Time_Out).until(
                    EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, locator)))
                objElement.click()
            elif locatorType.upper() == "TAGNAME":
                objElement = WebDriverWait(MyConfigFiles.driver, MyConfigFiles.Implicit_Time_Out).until(
                    EC.element_to_be_clickable((By.TAG_NAME, locator)))
                objElement.click()
            elif locatorType.upper() == "CLASSNAME":
                objElement = WebDriverWait(MyConfigFiles.driver, MyConfigFiles.Implicit_Time_Out).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, locator)))
                objElement.click()
            elif locatorType.upper() == "CSSSELECTOR":
                objElement = WebDriverWait(MyConfigFiles.driver, MyConfigFiles.Implicit_Time_Out).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))
                objElement.click()
            else:
                sys.exit(locatorType + " -Failed:: Select a valid locator type for "+locator)
            # print(locator + " -Success:: Clicked Element")

        except NoSuchElementException:
            sys.exit(locator + " -Failed:: No Such element found")

##Method to enter text in to a webEdit
# Parameters
#locator:value of the locator used
#locatorytype:Name of the locator used
#Value: Value to be passed
    def enterText(self,locator,locatorType,Value ):
        CL.CommonFunctions.presenceOfElement(self,locator,locatorType)
        try:
            if locatorType.upper() == "XPATH":
                MyConfigFiles.driver.find_element_by_xpath(locator).send_keys(Value)
            elif locatorType.upper() == "ID":
                MyConfigFiles.driver.find_element_by_id(locator).send_keys(Value)
            elif locatorType.upper() == "NAME":
                MyConfigFiles.driver.find_element_by_name(locator).send_keys(Value)
            elif locatorType.upper() == "lINKTEXT":
                MyConfigFiles.driver.find_element_by_link_text(locator).send_keys(Value)
            elif locatorType.upper() == "PARTIALLINKTEXT":
                MyConfigFiles.driver.find_element_by_partial_link_text(locator).send_keys(Value)
            elif locatorType.upper() == "TAGNAME":
                MyConfigFiles.driver.find_element_by_tag_name(locator).send_keys(Value)
            elif locatorType.upper() == "CLASSNAME":
                MyConfigFiles.driver.find_element_by_class_name(locator).send_keys(Value)
            elif locatorType.upper() == "CSSSELECTOR":
                MyConfigFiles.driver.find_element_by_css_selector(locator).send_keys(Value)
            else:
                sys.exit(locatorType + " -Failed:: Select a valid locator type for "+locator)
            # print(locator + " -Success:: Text entered")
        except NoSuchElementException:
            sys.exit(locator + "    Failed:: No Such element found")

# Method to select a value from the dropdown
# Parameters
#locator:value of the locator used
#locatorytype:Name of the locator used
# selectionType: DropDown selection type
# strValue: Value to be passed
    def selectDropdown(self,locator,locatorType, selectionType, DropDownValue):
        CL.CommonFunctions.presenceOfElement(self, locator, locatorType)
        try:
            if locatorType.upper() == "XPATH":
                objParent = Select(MyConfigFiles.driver.find_element_by_xpath(locator))
            elif locatorType.upper() == "ID":
                objParent = Select(MyConfigFiles.driver.find_element_by_id(locator))
            elif locatorType.upper() == "NAME":
                objParent = Select(MyConfigFiles.driver.find_element_by_name(locator))
            elif locatorType.upper() == "lINKTEXT":
                objParent = Select(MyConfigFiles.driver.find_element_by_link_text(locator))
            elif locatorType.upper() == "PARTIALLINKTEXT":
                objParent = Select(MyConfigFiles.driver.find_element_by_partial_link_text(locator))
            elif locatorType.upper() == "TAGNAME":
                objParent = Select(MyConfigFiles.driver.find_element_by_tag_name(locator))
            elif locatorType.upper() == "CLASSNAME":
                objParent = Select(MyConfigFiles.driver.find_element_by_class_name(locator))
            elif locatorType.upper() == "CSSSELECTOR":
                objParent = Select(MyConfigFiles.driver.find_element_by_css_selector(locator))
            else:
                sys.exit(locatorType + " -Failed:: Select a valid locator type for "+locator)
            counter = True

            if counter == True:
                if selectionType.upper() == "VALUE":
                    objParent.select_by_value(DropDownValue)
                elif selectionType.upper() == "INDEX":
                    objParent.select_by_index(DropDownValue)
                elif selectionType.upper() == "VISIBLETEXT":
                    objParent.select_by_visible_text(DropDownValue)
                else:
                    sys.exit(locator + " -Failed:: Please enter a valid selection Type")
                # print(locator + " -Success:: Selected the value based on "+selectionType)

        except NoSuchElementException:
            # print(locator + " -Failed:: No Such element found")
            sys.exit(locator + " -Failed:: No Such element found")

# Method to retrieve text from a webelement
# Parameters::
#locator:value of the locator used
#locatorytype:Name of the locator used

    def getText(self,locator,locatorType):
        CL.CommonFunctions.presenceOfElement(self, locator, locatorType)
        global strText
        try:
            if locatorType.upper() == "XPATH":
                objText = MyConfigFiles.driver.find_element_by_xpath(locator)
            elif locatorType.upper() == "ID":
                objText = MyConfigFiles.driver.find_element_by_id(locator)
            elif locatorType.upper() == "NAME":
                objText = MyConfigFiles.driver.find_element_by_name(locator)
            elif locatorType.upper() == "lINKTEXT":
                objText = MyConfigFiles.driver.find_element_by_link_text(locator)
            elif locatorType.upper() == "PARTIALLINKTEXT":
                objText = MyConfigFiles.driver.find_element_by_partial_link_text(locator)
            elif locatorType.upper() == "TAGNAME":
                objText = MyConfigFiles.driver.find_element_by_tag_name(locator)
            elif locatorType.upper() == "CLASSNAME":
                objText = MyConfigFiles.driver.find_element_by_class_name(locator)
            elif locatorType.upper() == "CSSSELECTOR":
                objText = MyConfigFiles.driver.find_element_by_css_selector(locator)
            else:
                sys.exit(locatorType + " -Failed:: Select a valid locator type for "+locator)
            strText = objText.text
            # print(locator + " -Success:: Text returned with value:" + strText)
            return strText

        except NoSuchElementException:
            sys.exit(locator + " -Failed:: No Such element found")

##To retrieve the URL from the loaded page
    def getURL(self):
        try:
            strTitle = MyConfigFiles.driver.current_url
            return strTitle
        except:
            print("Could not fetch the URL")


##To retrieve the count of similar elements on webpage
#Note: the xpath built should retrive the exact count of similar objects
#Parameters:
#locator:value of the locator used
#locatorytype:Name of the locator used


    def ElementCount(self,locator,locatorType):
        try:
            if locatorType.upper() == "XPATH":
                objInstance = MyConfigFiles.driver.find_elements_by_xpath(locator)
            elif locatorType.upper() == "ID":
                objInstance = MyConfigFiles.driver.find_elements_by_id(locator)
            elif locatorType.upper() == "NAME":
                objInstance = MyConfigFiles.driver.find_elements_by_name(locator)
            elif locatorType.upper() == "lINKTEXT":
                objInstance = MyConfigFiles.driver.find_elements_by_link_text(locator)
            elif locatorType.upper() == "PARTIALLINKTEXT":
                objInstance = MyConfigFiles.driver.find_elements_by_partial_link_text(locator)
            elif locatorType.upper() == "TAGNAME":
                objInstance = MyConfigFiles.driver.find_elements_by_tag_name(locator)
            elif locatorType.upper() == "CLASSNAME":
                objInstance = MyConfigFiles.driver.find_elements_by_class_name(locator)
            elif locatorType.upper() == "CSSSELECTOR":
                objInstance = MyConfigFiles.driver.find_elements_by_css_selector(locator)
            else:
                sys.exit(locatorType + " -Failed:: Select a valid locator type for " + locator)
            intCount = len(objInstance)
            # print(locator + " -Success:: Number of similar elements found:" + str(intCount))
            return intCount

        except NoSuchElementException:
            sys.exit(locator + " -Failed:: No Such element found")


##Method to check if the object exist
#Note: Test case will be failed if the assertion is failed(Hard Asert)
#Paramters
#locator: Value of the locator used
#locatorType: Name of the locator used
    def AssertObjectExists(self,locator,locatorType):
        CL.CommonFunctions.presenceOfElement(self,locator, locatorType)
        global strText
        try:
            if locatorType.upper() == "XPATH":
                MyConfigFiles.driver.find_element(By.XPATH, locator)
            elif locatorType.upper() == "ID":
                MyConfigFiles.driver.find_element(By.ID, locator)
            elif locatorType.upper() == "NAME":
                MyConfigFiles.driver.find_element(By.NAME, locator)
            elif locatorType.upper() == "lINKTEXT":
                MyConfigFiles.driver.find_element(By.LINK_TEXT, locator)
            elif locatorType.upper() == "PARTIALLINKTEXT":
                MyConfigFiles.driver.find_element(By.PARTIAL_LINK_TEXT, locator)
            elif locatorType.upper() == "TAGNAME":
                MyConfigFiles.driver.find_element(By.TAG_NAME, locator)
            elif locatorType.upper() == "CLASSNAME":
                MyConfigFiles.driver.find_element(By.CLASS_NAME, locator)
            elif locatorType.upper() == "CSSSELECTOR":
                MyConfigFiles.driver.find_element(By.CSS_SELECTOR, locator)
            else:
                sys.exit(locatorType + " -Failed:: Select a valid locator type for " + locator)
            print(locator + " -Assert:: Object is displayed")

        except:
            sys.exit(locator+"--Object is not displayed")
        return True


##Method to check if the object exist
#Note: Test case will be not failed if the assertion is failed(Soft Asert)
#Paramters
#locator: Value of the locator used
#locatorType: Name of the locator used
    def ObjectExists(self, locator, locatorType):
        CL.CommonFunctions.presenceOfElement(self, locator, locatorType)
        global strText
        try:
            if locatorType.upper() == "XPATH":
                MyConfigFiles.driver.find_element(By.XPATH, locator)
            elif locatorType.upper() == "ID":
                MyConfigFiles.driver.find_element(By.ID, locator)
            elif locatorType.upper() == "NAME":
                MyConfigFiles.driver.find_element(By.NAME, locator)
            elif locatorType.upper() == "lINKTEXT":
                MyConfigFiles.driver.find_element(By.LINK_TEXT, locator)
            elif locatorType.upper() == "PARTIALLINKTEXT":
                MyConfigFiles.driver.find_element(By.PARTIAL_LINK_TEXT, locator)
            elif locatorType.upper() == "TAGNAME":
                MyConfigFiles.driver.find_element(By.TAG_NAME, locator)
            elif locatorType.upper() == "CLASSNAME":
                MyConfigFiles.driver.find_element(By.CLASS_NAME, locator)
            elif locatorType.upper() == "CSSSELECTOR":
                MyConfigFiles.driver.find_element(By.CSS_SELECTOR, locator)
            else:
                sys.exit(locatorType + " -Failed:: Select a valid locator type for " + locator)
            print(locator + " -Assert:: Object is displayed")
            return True
        except:
            print(locator + "--Object is not displayed")
        return False

##Method to retrieve Function name
    def getFunctionName(self):
        try:
            this_function_name = sys._getframe(2).f_code.co_name
            return this_function_name
        except:
            print("Failed:: Verify to get the parent function name")

##Method to retrieve current working directory
    def getCurrentDirectory(self):
        try:
            this_current_dir = os.getcwd()
            return this_current_dir
        except:
            print(" Failed:: Verify to get the current directory")


#method to create a new directory
    def createdirectory(WorkingDirectory):
        if not os.path.exists(WorkingDirectory):
            os.makedirs(WorkingDirectory)
            #print("Directory ", WorkingDirectory, " Created ")
        else:
            pass
            #print("Directory ", WorkingDirectory, " already exists")

    def ValidationOnSelectedtext(self, locator, locatorType):
        try:
            if locatorType.upper() == "XPATH":
                objInstance = Select(MyConfigFiles.driver.find_element_by_xpath(locator))
                objget = objInstance.first_selected_option
            elif locatorType.upper() == "ID":
                 objInstance = Select(MyConfigFiles.driver.find_element_by_id(locator))
                 objget = objInstance.first_selected_option
            elif locatorType.upper() == "NAME":
                 objInstance = Select(MyConfigFiles.driver.find_element_by_name(locator))
                 objget = objInstance.first_selected_option
            elif locatorType.upper() == "lINKTEXT":
                 objInstance = Select(MyConfigFiles.driver.find_element_by_link_text(locator))
                 objget = objInstance.first_selected_option
            elif locatorType.upper() == "PARTIALLINKTEXT":
                 objInstance = Select(MyConfigFiles.driver.find_element_by_partial_link_text(locator))
                 objget = objInstance.first_selected_option
            elif locatorType.upper() == "TAGNAME":
                 objInstance = Select(MyConfigFiles.driver.find_element_by_tag_name(locator))
                 objget = objInstance.first_selected_option
            elif locatorType.upper() == "CLASSNAME":
                 objInstance = Select(MyConfigFiles.driver.find_element_by_class_name(locator))
                 objget = objInstance.first_selected_option
            elif locatorType.upper() == "CSSSELECTOR":
                 objInstance = Select(MyConfigFiles.driver.find_element_by_css_selector(locator))
                 objget = objInstance.first_selected_option
            else:
                sys.exit(locatorType + " -Failed:: Select a valid locator type for " + locator)
            print(locator + " -Assert:: Object is displayed")
            objvalue = objget.text
            return objvalue
        except:
            sys.exit(locator + "--Object is not displayed")


    def getAttributeValue(self, locator, locatorType, attributeName):
         CL.CommonFunctions.presenceOfElement(self, locator, locatorType)
         global strText
         try:
            if locatorType.upper() == "XPATH":
               objText = MyConfigFiles.driver.find_element_by_xpath(locator)
            elif locatorType.upper() == "ID":
               objText = MyConfigFiles.driver.find_element_by_id(locator)
            elif locatorType.upper() == "NAME":
               objText = MyConfigFiles.driver.find_element_by_name(locator)
            elif locatorType.upper() == "lINKTEXT":
               objText = MyConfigFiles.driver.find_element_by_link_text(locator)
            elif locatorType.upper() == "PARTIALLINKTEXT":
               objText = MyConfigFiles.driver.find_element_by_partial_link_text(locator)
            elif locatorType.upper() == "TAGNAME":
               objText = MyConfigFiles.driver.find_element_by_tag_name(locator)
            elif locatorType.upper() == "CLASSNAME":
               objText = MyConfigFiles.driver.find_element_by_class_name(locator)
            elif locatorType.upper() == "CSSSELECTOR":
               objText = MyConfigFiles.driver.find_element_by_css_selector(locator)
            else:
                sys.exit(locatorType + " -Failed:: Select a valid locator type for " + locator)
            strText = objText.get_attribute(attributeName)
        # print(locator + " -Success:: Text returned with value:" + strText)
            return strText
         except NoSuchElementException:
           sys.exit(locator + " -Failed:: No Such element found")



    def Page_Scroll_Actions(self,locator,locatorType ):
        CL.CommonFunctions.presenceOfElement(self,locator,locatorType)
        try:
            if locatorType.upper() == "XPATH":
                actions = ActionChains(MyConfigFiles.driver)
                element= MyConfigFiles.driver.find_element_by_xpath(locator)
                actions.move_to_element(element)
                actions.perform()
            elif locatorType.upper() == "ID":
                actions = ActionChains(MyConfigFiles.driver)
                element=MyConfigFiles.driver.find_element_by_id(locator)
                actions.move_to_element(element)
                actions.perform()
            elif locatorType.upper() == "NAME":
                actions = ActionChains(MyConfigFiles.driver)
                element=MyConfigFiles.driver.find_element_by_name(locator)
                actions.move_to_element(element)
                actions.perform()
            elif locatorType.upper() == "lINKTEXT":
                actions = ActionChains(MyConfigFiles.driver)
                element=MyConfigFiles.driver.find_element_by_link_text(locator)
                actions.move_to_element(element)
                actions.perform()
            elif locatorType.upper() == "PARTIALLINKTEXT":
                actions = ActionChains(MyConfigFiles.driver)
                element=MyConfigFiles.driver.find_element_by_partial_link_text(locator)
                actions.move_to_element(element)
                actions.perform()
            elif locatorType.upper() == "TAGNAME":
                actions = ActionChains(MyConfigFiles.driver)
                element=MyConfigFiles.driver.find_element_by_tag_name(locator)
                actions.move_to_element(element)
                actions.perform()
            elif locatorType.upper() == "CLASSNAME":
                actions = ActionChains(MyConfigFiles.driver)
                element = MyConfigFiles.driver.find_element_by_class_name(locator)
                actions.move_to_element(element)
                actions.perform()
            elif locatorType.upper() == "CSSSELECTOR":
                actions = ActionChains(MyConfigFiles.driver)
                element=MyConfigFiles.driver.find_element_by_css_selector(locator)
                actions.move_to_element(element)
                actions.perform()

            else:
                sys.exit(locatorType + " -Failed:: Select a valid locator type for "+locator)
            # print(locator + " -Success:: Text entered")
        except NoSuchElementException:
            sys.exit(locator + "    Failed:: No Such element found")
