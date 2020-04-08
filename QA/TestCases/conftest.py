from QA.Utilities.CommonLib import CommonFunctions
from QA.Base.Config import MyConfigFiles
import pytest
from QA.Utilities.PerformAction import PerformActions
import shutil
import time
import os



global objCommonLib
objCommonLib=CommonFunctions()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test executes.
    :param item:
    """
    global itr
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    report.description = str(item.function.__doc__)
    report.function = item.function.__doc__
    report_directory = os.path.dirname(item.config.option.htmlpath)

    if report.when == 'call' or report.when == "setup":
        extra.append(pytest_html.extras.url(MyConfigFiles.AppURL))
        xfail = hasattr(report, 'wasxfail')
        #print("Xfaile details::", xfail)
        if report.outcome == "passed":
            file_name = report.nodeid.replace("QA/TestCases/", '\\')
            file_name = file_name.replace("::", "_")
            print("passed:: ", file_name)
        if (report.skipped and xfail) or (report.failed and not xfail):  # or report.outcome:
            #print("Report . Node ID::", report.nodeid)
            if MyConfigFiles.Environment.upper() == "LOCAL":
                file_name = report.nodeid.replace("QA/TestCases/", '\\')
            elif MyConfigFiles.Environment.upper() == "REMOTE":
                file_name = report.nodeid.replace("QA/TestCases/", '//')

            file_name = file_name.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            extra.append(pytest_html.extras.html('<div>Log description</div>'))
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
                print("Failed:: ", file_name)
            # movfiletodir(file_name)
        report.extra = extra


def _capture_screenshot(name):
    if MyConfigFiles.Environment.upper() == "LOCAL":
        screenShot_ReportFile_Path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"TestReport\\")
    elif MyConfigFiles.Environment.upper() == "REMOTE":
        screenShot_ReportFile_Path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"TestReport//")
    MyConfigFiles.driver.get_screenshot_as_file(screenShot_ReportFile_Path + name)

#make scope is uncomment if you login and logout onnly once
# @pytest.fixture (scope='module', autouse=True
@pytest.fixture (scope='session')
def setup():
    objCommonLib.LaunchBrowser()

    yield
    objCommonLib.CloseBrowser()
    MyConfigFiles.driver=None

@pytest.fixture()
def TestData():
    global objDataList
    objData = CommonFunctions()
    objDataList = objData.readExcelData()

    if len(objDataList)==1:
        for objDic in objDataList:
            return objDic
    else:                               #returns a datalist in case of bulk data for single test case[use for loop to access a dictionary out of the list]
        return objDataList


def movfiletodir(file_name):
    PerformActions.createdirectory(MyConfigFiles.ScreenShot_ReportFile_Path + 'Failed')
    shutil.move(MyConfigFiles.ScreenShot_ReportFile_Path + file_name, MyConfigFiles.ScreenShot_ReportFile_Path + 'Failed')












