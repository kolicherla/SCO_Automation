from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.microsoft import IEDriverManager
from QA.Utilities.PerformAction import PerformActions
from selenium.webdriver.common.by import By
from QA.Base.Config import MyConfigFiles
from selenium.common import exceptions
from dateutil.relativedelta import *
from selenium import webdriver
from pytz import timezone
from pathlib import Path
import pandas as pd
import datetime
import base64
import pytest
import time
import os
import sys



class CommonFunctions():
    # Method Name: readExcelData
    # Owner:
    # Comments: Capibility to fetch single and bulk data at a time.
    # Usage: NA
    # Execution Comments: Automatically executes at the beginning of every test case
    def readExcelData(self):
        global data_dic, flag
        TCname = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0].replace('test_', "")
        Appname = TCname.split('_')[1]
        strFileName = Appname + "_Module.csv"

        # Data file path
        if MyConfigFiles.Environment.upper()=="LOCAL":
            TestDataLoc = os.path.join(os.path.dirname(os.getcwd())) + "\\TestData\\" + strFileName.strip()
        elif MyConfigFiles.Environment.upper()=="REMOTE":
            TestDataLoc = os.path.join(os.path.dirname(os.getcwd())) + "//TestData//" + strFileName.strip()

        # verify if the file is present(hard exit)
        if Path(TestDataLoc).is_file():
            pass
        else:
            pytest.exit('Could not find the Test Data file in the below location :' + str(TestDataLoc))

        strData = pd.read_csv(TestDataLoc)       #reading csv
        dfData = pd.DataFrame(strData)           #converting the read data to dataframe
        # print(dfData)
        rowcount = dfData.shape[0]
        colcount = dfData.shape[1]
                                                #initializing the variables
        TcCount = 0
        TcRowNum = []
        for i in range(0, rowcount):            #reading entire sheet to find similar data
            strTCName = dfData.iloc[i, 0]
            if strTCName == TCname:
                TcCount = TcCount + 1
                TcRowNum.append(i)

        if TcCount == 0:
            sys.exit("Could not find the test case Name")
        print("Similar test cases found:" + str(TcCount))
        TcNum = 0
        dataList = []
        for Tc in TcRowNum:
            TcNum = TcNum + 1
            data_dic = {}
            for col in range(0, colcount):
                name = dfData.iloc[Tc - TcNum, col]
                value = dfData.iloc[Tc, col]
                data_dic[name] = value               #writing the data into a dictionary
            dataList.append(data_dic)               #Creating a list of dictionaries
        return dataList



    # Method Name: SelectBrowser
    # Owner:
    # Comments: browser seleciton based on the browser type sent from config.py file.
    #           Uses webdriver manager for local execution and headless browser for remote execution.
    # Usage: NA (automatically executes by the setup fixture)
    #Execution Comments: Invoked by Launchbrowser method
    def SelectBrowser(self,BrowserType):
        if BrowserType.upper() == 'BS' or BrowserType.upper()=='BrowserStack':                  #browser stack
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
                command_executor='http://tanushree7:xS4ja396QyXd8T5mVqxu@hub.browserstack.com:80/wd/hub',               #logs in automatically using the url
                desired_capabilities=desired_cap)

        ####*************Currently the execution on remote server happens only on google chrome, aiming for other browser types in future
        elif BrowserType.upper() == 'GC' or BrowserType.upper()=='GOOGLE CHROME':
            if MyConfigFiles.Environment.upper()=="REMOTE":                #uses headless brower
                options = webdriver.ChromeOptions()
                options.add_argument('--no-sandbox')
                options.add_argument('--headless')
                options.add_argument('--disable-gpu')
                options.add_argument("--window-size=1325x744")
                MyConfigFiles.driver = webdriver.Chrome(options=options,
                                                        service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])
            else:
                MyConfigFiles.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

        elif BrowserType.upper() == 'FF' or BrowserType.upper() =='FIREFOX':
            MyConfigFiles.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

        elif BrowserType.upper() == 'IE' or BrowserType.upper() =='INTERNET EXPLORER':
            MyConfigFiles.driver = webdriver.Ie(executable_path=IEDriverManager('3.141.0').install())

        else:
            pytest.exit('Could not find the driver with name :'+BrowserType)



    # Method Name: LaunchBrowser
    # Owner:
    # Comments: Launches the browser depending on the browser selected
    # Usage: LaunchBrowser(AppURL)
    #execution Comments: Invoked by setup fixture
    def LaunchBrowser(self):
        self.SelectBrowser(MyConfigFiles.BrowserType)


    def LoadURL(self,AppURL):
        try:
            MyConfigFiles.driver.get(AppURL)
            MyConfigFiles.driver.maximize_window()
            time.sleep(5)
            self.compareBrowserTitle()
        except exceptions.InvalidSessionIdException:
            print("Invalid session token, relaunching the browser")

    # Method Name: compareBrowserTitle
    # Owner:
    # Comments: Compares the Runtime brower title with the Test browser title.
    #           Refreshes the page for 5 iterations until the broswer title is matched.
    # Usage: compareBrowserTitle
    #Execution Comments: Invoked by launchBrowser method
    def compareBrowserTitle(self):
        strTitle = MyConfigFiles.driver.title
        print("Title of the application displayed: " + strTitle)
        iteration = 0
        while strTitle != MyConfigFiles.App_Title and iteration < 5:                #iterating until the title is matched for 5 iterations
            iteration += 1
            print("Information:: Browser title did not match,Refreshing the page for iteration:" + str(iteration))
            MyConfigFiles.driver.refresh()
            time.sleep(2)
            strTitle = MyConfigFiles.driver.title
        if strTitle != MyConfigFiles.App_Title:
            sys.exit("Browser title did not match even after refresing the page")



    # Method Name: CloseBrowser
    # Owner:
    # Comments: Method to close active browsers
    # Usage: CloseBrowser()
    # Execution Comments: Invoked by yield in conftest as part of fixture.
    #                     Include this method at the end of the test case if necessary
    def CloseBrowser(self):
        MyConfigFiles.driver.close()
        MyConfigFiles.driver.quit()


    # Method Name: capture_screenshot
    # Owner:
    # Comments: Captures the screenshot of the application and stores it in .png format
    #           Screen captures are stored in TestReport folder in the hierarchy[TestReport/ScreenShots/ModuleName/TestCaseName]
    # Usage: capture_screenshot("Text")
    # Execution Comments: call the method at the end of every operations.
    def capture_screenshot(self, FileName):
        time.sleep(2)
        if MyConfigFiles.Environment.upper() == "LOCAL":
            ScreenShot_ReportFile_Path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                                      "TestReport\\")
        elif MyConfigFiles.Environment.upper() == "REMOTE":
            ScreenShot_ReportFile_Path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                                  "TestReport//")
        TCname = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0].replace('test_', "")
        # caller function and its module name
        Appname = TCname.split('_')[1] + "_Module"
        WorkingDirectory = os.path.join(ScreenShot_ReportFile_Path, 'ScreenShots', Appname,TCname)  # Create target Directory if don't exist
        PerformActions.createdirectory(WorkingDirectory)
        strTime = time.asctime().split(' ')
        MyConfigFiles.driver.get_screenshot_as_file(WorkingDirectory + '/' + strTime[3]+'_'+strTime[4].replace(':', '') + '_' + FileName + '.png')

    # Method Name: presenceOfElement
    # Owner:
    # Comments: Verifies if an element is present
    # Usage: presenceOfElement("Attribute Value","Attribute Name")
    # Execution Comments: Invoked by the methods in performActions.
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



    # Method Name: ElementClickable
    # Owner:
    # Comments: Verifies if an element is clickable
    # Usage: ElementClickable("Attribute Value","Attribute Name")
    # Execution Comments: Invoked by clickElement method in performActions.
    def ElementClickable(self, locator, locatorType):
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
            print(locator + ":: Failed -Element is not clickable")




    # Method Name: GetCurrentDate
    # Owner:
    # Comments: retrieves the date of US/Pacific region in the format of MM/DD/YYYY
    # Usage: GetCurrentDate()
    # Execution Comments:
    def GetCurrentDate(self):
        today = datetime.datetime.now(timezone('US/Pacific'))
        strDate = today.strftime("%m/%d/%Y")
        return strDate



    # Method Name: GetCurrentDay
    # Owner:
    # Comments: retrieves current day of US/Pacific region in the format of DD
    # Usage: GetCurrentDay()
    # Execution Comments: if the date is less than 10, 0 will be replaced with null.
    def GetCurrentDay(self):
        today = datetime.datetime.now(timezone('US/Pacific'))
        strUpdatedDay = today.strftime("%d")
        if int(strUpdatedDay) < 10:
            strUpdatedDay = strUpdatedDay.replace("0", '')
        return strUpdatedDay




    # Method Name: ModifyDateWithOutWeekends
    # Owner:
    # Comments: This Method can perform operations(addition and substraction) on the current date and retrieves the date in mm/dd/yyyy format
    # Usage: ModifyDateWithOutWeekends()
    # Execution Comments: ignores weekends while performing operations.
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




    # Method Name: ModifyDay
    # Owner:
    # Comments: This Method can perform operations(addition and substraction) on the current date and retrieves the date in dd format
    # Usage: ModifyDay(operation, add_days)
    # Execution Comments: perform operations on current day.
    def ModifyDay(self, operation, add_days):
        UScurrent_date = datetime.datetime.now(timezone('US/Pacific'))
        if operation.upper() == "ADD":
            UScurrent_date += datetime.timedelta(days=int(add_days))
            print(UScurrent_date)

        elif operation.upper() == "SUB":
            UScurrent_date -= datetime.timedelta(days=add_days)

        return UScurrent_date.strftime("%d")



    # Method Name: ModifyDate
    # Owner:
    # Comments: This Method can perform operations(addition and substraction) on the current date and retrieves the date in mm/dd/yyyy format
    # Usage: ModifyDate(operation, add_days)
    # Execution Comments: perform operations on current date.
    def ModifyDate(self, operation, add_days):
        UScurrent_date = datetime.datetime.now(timezone('US/Pacific'))
        print(UScurrent_date)
        if operation.upper() == "ADD":
            UScurrent_date += datetime.timedelta(days=int(add_days))

        elif operation.upper() == "SUB":
            UScurrent_date -= datetime.timedelta(days=int(add_days))

        return UScurrent_date.strftime("%m/%d/%Y")


    # Method Name: ModifyMonth
    # Owner:
    # Comments: This Method can perform operations(addition and substraction) on the current moth and retrieves the month in mm format
    # Usage: ModifyMonth(operation, add_months)
    # Execution Comments: perform operations on current month
    def ModifyMonth(self, operation, add_months):
        start_date = datetime.datetime.now(timezone('US/Pacific'))
        # print(UScurrent_date)
        if operation.upper() == "ADD":
            start_date = start_date+relativedelta(months=+int(add_months))
        elif operation.upper() == "SUB":
            start_date = start_date+relativedelta(months=-int(add_months))
        return start_date.strftime("%m/%d/%Y")



    # Method Name: ModifyDateFrom
    # Owner:
    # Comments: This Method can perform operations(addition and substraction) on the specified date and retrieves the date in mm/dd/yyyy format
    # Usage: ModifyDateFrom(startDate,operation, add_days)
    # Execution Comments: perform operations starting from the date provided
    def ModifyDateFrom(self,startDate,operation, add_days):
        UScurrent_date = datetime.datetime.strptime(startDate,'%m/%d/%Y')
        print(UScurrent_date)
        if operation.upper() == "ADD":
            UScurrent_date += datetime.timedelta(days=int(add_days))

        elif operation.upper() == "SUB":
            UScurrent_date -= datetime.timedelta(days=int(add_days))

        return UScurrent_date.strftime("%m/%d/%Y")


    # Method Name: AttachFile
    # Owner:
    # Comments: This method is used to attach files
    # Usage: AttachFile(fileName, locatorType, locator)
    # Execution Comments: Attach the file in the folder structure with the folder name as Attachments.
    def AttachFile(self, fileName, locatorType, locator):
        global objActions
        objActions = PerformActions()
        if MyConfigFiles.Environment.upper() == "LOCAL":
            strFilePath = os.path.join(os.path.dirname(os.getcwd())) + '\\Attachments\\' + fileName + '.xlsx'.strip()
        elif MyConfigFiles.Environment.upper() == "REMOTE":
            strFilePath = os.path.join(os.path.dirname(os.getcwd())) + '//Attachments//' + fileName + '.xlsx'.strip()
        if Path(strFilePath).is_file():
            objActions.enterText(locatorType, locator, strFilePath)
            time.sleep(2)
            print("FIle uploaded sucessfully")
        else:
            print("could not find the file to uplaod")



