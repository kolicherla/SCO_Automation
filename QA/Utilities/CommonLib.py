from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.microsoft import IEDriverManager
from QA.Utilities.PerformAction import PerformActions
from selenium.webdriver.common.by import By
from QA.Base.Config import MyConfigFiles
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pytz import timezone
from pathlib import Path
import datetime
import inspect
import base64
import pytest
import xlrd
import time
import sys
import os



class CommonFunctions():
    # reading data from excel sheet
    def readExcelData(self):
        global data_dic,flag
        TestDataLoc=os.path.join(os.path.dirname(os.getcwd()))+'\TestData\SCO_TestData.xlsx'.strip()
        TCname=os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0].replace('test_',"")

        #verify if the file is present
        if Path(TestDataLoc).is_file():
            pass
        else:
            pytest.exit('Could not find the Test Data file in the below location :'+str(TestDataLoc))

        Appname = TCname.split('_')[1]
        objWorkbook = xlrd.open_workbook(TestDataLoc)
        try:
            objSheet = objWorkbook.sheet_by_name(Appname)
        except:
            sys.exit('Could not find the sheet with name:'+Appname)

        data_dic={}
        for row in range(0,objSheet.nrows):
            data=objSheet.cell_value(row,0)
            if data==TCname:
                flag=True
                break
            else:
                flag=False
        if flag != True:
            sys.exit('Could not find the Test Case:'+TCname+'  -  '+'In Sheet:'+Appname)

        for col in range(0,objSheet.ncols):
            name=objSheet.cell(row-1,col).value
            value=objSheet.cell(row,col).value
            data_dic[name]=value
        return data_dic


#Select the browser
    def SelectBrowser(self,BrowserType):
        if BrowserType.upper() == 'BS' or BrowserType.upper()=='BrowserStack':
            desired_cap = {
                'os': 'Windows',
                'os_version': '10',
                'browser': 'Chrome',
                'browser_version': '64.0',
                'project': 'QET_SCAR_Login',
                'build': '1',
                'name': 'Edge_LoginandScarLink',
                'browserstack.local': 'true',
                'browserstack.debug': 'true',
                'browserstack.timezone': 'chennai',
                'browserstack.selenium_version': '2.53.0',
                'acceptSslCerts': 'true'
            }
            MyConfigFiles.driver = webdriver.Remote(
                command_executor='http://tanushree7:xS4ja396QyXd8T5mVqxu@hub.browserstack.com:80/wd/hub',
                desired_capabilities=desired_cap)

        elif BrowserType.upper() == 'GC' or BrowserType.upper()=='GOOGLE CHROME':
            MyConfigFiles.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

        elif BrowserType.upper() == 'FF' or BrowserType.upper() =='FIREFOX':
            MyConfigFiles.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

        elif BrowserType.upper() == 'IE' or BrowserType.upper() =='INTERNET EXPLORER':
            MyConfigFiles.driver = webdriver.Ie(executable_path=IEDriverManager('3.141.0').install())

        else:
            pytest.exit('Could not find the driver with name :'+BrowserType)


#Method to capture screenshot
    def capture_screenshot(self, FileName):
        time.sleep(2)
        ScreenShot_ReportFile_Path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                                  "TestReport\\")
        TCname = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0].replace('test_', "")
        # caller function and its module name
        Appname = TCname.split('_')[1] + "_Module"
        WorkingDirectory = os.path.join(ScreenShot_ReportFile_Path, 'ScreenShots', Appname,TCname)  # Create target Directory if don't exist
        PerformActions.createdirectory(WorkingDirectory)
        strTime = time.asctime().split(' ')
        MyConfigFiles.driver.get_screenshot_as_file(WorkingDirectory + '/' + strTime[3].replace(':', '') + '_' + FileName + '.png')

#Method to check for the presence of element
    def presenceOfElement(self,locator,locatorType):
        try:
            if locatorType.upper() == "ID":
                WebDriverWait(MyConfigFiles.driver, MyConfigFiles.Implicit_Time_Out).until(
                    EC.presence_of_element_located((By.ID, locator)))

            elif locatorType.upper() == "NAME":
                WebDriverWait(MyConfigFiles.driver, MyConfigFiles.Implicit_Time_Out).until(
                    EC.presence_of_element_located((By.NAME, locator)))

            elif locatorType.upper() == "XPATH":
                WebDriverWait(MyConfigFiles.driver, MyConfigFiles.Implicit_Time_Out).until(
                    EC.presence_of_element_located((By.XPATH, locator)))

            elif locatorType.upper() == "lINKTEXT":
                WebDriverWait(MyConfigFiles.driver, MyConfigFiles.Implicit_Time_Out).until(
                    EC.presence_of_element_located((By.LINK_TEXT, locator)))

            elif locatorType.upper() == "PARTIALLINKTEXT":
                WebDriverWait(MyConfigFiles.driver, MyConfigFiles.Implicit_Time_Out).until(
                    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, locator)))

            elif locatorType.upper() == "TAGNAME":
                WebDriverWait(MyConfigFiles.driver, MyConfigFiles.Implicit_Time_Out).until(
                    EC.presence_of_element_located(MyConfigFiles.driver.find_element_by_tag_name(locator)))

            elif locatorType.upper() == "CLASSNAME":
                WebDriverWait(MyConfigFiles.driver, MyConfigFiles.Implicit_Time_Out).until(
                    EC.presence_of_element_located((By.CLASS_NAME, locator)))

            elif locatorType.upper() == "CSSSELECTOR":
                WebDriverWait(MyConfigFiles.driver, MyConfigFiles.Implicit_Time_Out).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, locator)))

        except TimeoutException:
            print(locator+ "-Loading of the Element took too much time")

#Method to launch the browser
    def LaunchBrowser(self,AppURL):
        global objCommFn
        objCommFn = CommonFunctions()
        objCommFn.SelectBrowser(MyConfigFiles.BrowserType)
        MyConfigFiles.driver.implicitly_wait(MyConfigFiles.Implicit_Time_Out)
        MyConfigFiles.driver.get(AppURL)
        MyConfigFiles.driver.maximize_window()


#Method to close the browser
    def CloseBrowser(self):
        MyConfigFiles.driver.close()
        # MyConfigFiles.driver.quit()

#retrieves US/Pacific date in MM/DD/YYYY format
    def GetCurrentDate(self):
        today = datetime.datetime.now(timezone('US/Pacific'))
        strDate = today.strftime("%m/%d/%Y")
        return strDate

# retrieves date in DD format
    def GetCurrentDay(self):
        today = datetime.datetime.now(timezone('US/Pacific'))
        strUpdatedDay = today.strftime("%d")
        strDay=str(strUpdatedDay).replace("0", '')
        return strDay

#This Method can perform operations(addition and substraction) on the current date and retrieves the date in mm/dd/yyyy format
    def ModifyDateWithOutWeekends(self,operation, add_days):
        UScurrent_date = datetime.datetime.now(timezone('US/Pacific'))
        if operation.upper() == "ADD":
            while add_days > 0:
                UScurrent_date += datetime.timedelta(days=1)
                weekday = UScurrent_date.weekday()
                if weekday >= 5:
                    continue
                add_days -= 1
        elif operation.upper() == "SUB":
            while add_days > 0:
                UScurrent_date -= datetime.timedelta(days=1)
                weekday = UScurrent_date.weekday()
                if weekday >= 5:
                    continue
                add_days -= 1

        return UScurrent_date.strftime("%m/%d/%Y")

# This Method can perform operations(addition and substraction) on the current date and retrieves the date in dd format
    def ModifyDay(self, operation, add_days):
        UScurrent_date = datetime.datetime.now(timezone('US/Pacific'))
        print(UScurrent_date)
        if operation.upper() == "ADD":
            UScurrent_date += datetime.timedelta(days=add_days)

        elif operation.upper() == "SUB":
            UScurrent_date -= datetime.timedelta(days=add_days)

        return UScurrent_date.strftime("%d")

# This Method can perform operations(addition and substraction) on the current date and retrieves the date in mm/dd/yyyy format
    def ModifyDate(self, operation, add_days):
        UScurrent_date = datetime.datetime.now(timezone('US/Pacific'))
        print(UScurrent_date)
        if operation.upper() == "ADD":
            UScurrent_date += datetime.timedelta(days=add_days)

        elif operation.upper() == "SUB":
            UScurrent_date -= datetime.timedelta(days=add_days)

        return UScurrent_date.strftime("%m/%d/%Y")


    # This Method can perform operations(addition and substraction) on the current date and retrieves the date in mm/dd/yyyy format
    def ModifyMonth(self, operation, add_Months):
        UScurrent_date = datetime.datetime.now(timezone('US/Pacific'))
        print(UScurrent_date)
        if operation.upper() == "ADD":
            UScurrent_date += datetime.timedelta(MONTHS=add_Months)
        elif operation.upper() == "SUB":
            UScurrent_date -= datetime.timedelta(MONTHS=add_Months)

        return UScurrent_date.strftime("%m/%d/%Y")


# This Method can perform operations(addition and substraction) on the specified date and retrieves the date in mm/dd/yyyy format
    def ModifyDateFrom(self,startDate,operation, add_days):
        UScurrent_date = datetime.datetime.strptime(startDate,'%m/%d/%Y')
        print(UScurrent_date)
        if operation.upper() == "ADD":
            UScurrent_date += datetime.timedelta(days=add_days)

        elif operation.upper() == "SUB":
            UScurrent_date -= datetime.timedelta(days=add_days)

        return UScurrent_date.strftime("%m/%d/%Y")





#Method to verify if the object is clickable
#Parameters:
#locator: Value of the locator
#locatorType: Name of the locator used
    def ElementClickable(self,locator,locatorType):
        try:
            if locatorType.upper() == "ID":
                WebDriverWait(MyConfigFiles.driver, MyConfigFiles.Implicit_Time_Out).until(
                    EC.element_to_be_clickable((By.ID, locator)))

            elif locatorType.upper() == "NAME":
                WebDriverWait(MyConfigFiles.driver, MyConfigFiles.Implicit_Time_Out).until(
                    EC.element_to_be_clickable((By.NAME, locator)))

            elif locatorType.upper() == "XPATH":
                WebDriverWait(MyConfigFiles.driver, MyConfigFiles.Implicit_Time_Out).until(
                    EC.element_to_be_clickable((By.XPATH, locator)))

            elif locatorType.upper() == "lINKTEXT":
                WebDriverWait(MyConfigFiles.driver, MyConfigFiles.Implicit_Time_Out).until(
                    EC.element_to_be_clickable((By.LINK_TEXT, locator)))

            elif locatorType.upper() == "PARTIALLINKTEXT":
                WebDriverWait(MyConfigFiles.driver, MyConfigFiles.Implicit_Time_Out).until(
                    EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, locator)))

            elif locatorType.upper() == "TAGNAME":
                WebDriverWait(MyConfigFiles.driver, MyConfigFiles.Implicit_Time_Out).until(
                    EC.element_to_be_clickable(MyConfigFiles.driver.find_element_by_tag_name(locator)))

            elif locatorType.upper() == "CLASSNAME":
                WebDriverWait(MyConfigFiles.driver, MyConfigFiles.Implicit_Time_Out).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, locator)))

            elif locatorType.upper() == "CSSSELECTOR":
                WebDriverWait(MyConfigFiles.driver, MyConfigFiles.Implicit_Time_Out).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))

        except TimeoutException:
            print(locator +":: Failed -Element is not clickable")

#Method to decrypt the password using base64 package
    def DecryptPassword(self,Password):
        try:
            strTune = Password.replace('"', "")
            strDecrypt = strTune.encode('utf-8')
            strPassword = base64.b64decode(strDecrypt).decode('utf-8')
            return strPassword
        except:
            print("Could not decrypt the password")

    def get_clear_browsing_button(self):
        """Find the "CLEAR BROWSING BUTTON" on the Chrome settings page."""
        return MyConfigFiles.driver.find_element_by_xpath("//*[@id='clearBrowsingDataConfirm']")

    def clear_cache(self):
        MyConfigFiles.driver.delete_all_cookies()

        MyConfigFiles.driver.get('chrome://settings/clearBrowserData')
        # wait for the button to appear
        # wait = WebDriverWait(MyConfigFiles.driver, MyConfigFiles.Implicit_Time_Out)
        # wait.until(self.get_clear_browsing_button())
        time.sleep(5)
        # click the button to clear the cache
        MyConfigFiles.driver.find_element_by_css_selector('cr-button#clearBrowsingDataConfirm').click()
        # wait for the button to be gone before returning
        # wait.until_not(self.get_clear_browsing_button())



