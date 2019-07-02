from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from QA.Utilities.PerformAction import PerformActions
from QA.Base.Config import MyConfigFiles
from selenium import webdriver
from pathlib import Path
import inspect
import pytest
import time
import xlrd
import sys
import os

#reading data from excel
class CommonFunctions():

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
        if BrowserType.upper() == 'GC' or BrowserType.upper()=='GOOGLE CHROME':
            MyConfigFiles.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

        elif BrowserType.upper() == 'FF' or BrowserType.upper() =='FIREFOX':
            MyConfigFiles.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

        elif BrowserType.upper() == 'IE' or BrowserType.upper() =='INTERNET EXPLORER':
            MyConfigFiles.driver = webdriver.Ie(executable_path=IEDriverManager('3.141.0').install())

        else:
            pytest.exit('Could not find the driver with name :'+BrowserType)


    #captures screenshot as per the filename
    def capture_screenshot(self,FileName):
        ScreenShot_ReportFile_Path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"TestReport\\")
        TCname = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0].replace('test_', "")
        #caller function and its module name
        frm = inspect.stack()[1]
        ModuleName = inspect.getmodule(frm[0]).__name__.replace('QA.TestCases.',"")
        # Create target Directory if don't exist
        WorkingDirectory = os.path.join(ScreenShot_ReportFile_Path, 'ScreenShots', ModuleName, TCname)
        PerformActions.createdirectory(WorkingDirectory)
        strTime = time.asctime().split(' ')
        MyConfigFiles.driver.get_screenshot_as_file(WorkingDirectory + '/' + strTime[4].replace(':', '')+ '_' +FileName+'.png')
