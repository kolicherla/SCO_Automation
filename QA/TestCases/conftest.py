from QA.Utilities.CommonLib import CommonFunctions
from QA.Base.Config import MyConfigFiles
import pytest
from QA.Utilities.PerformAction import PerformActions
import shutil
import os



global objCommonLib
objCommonLib=CommonFunctions()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test executes.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    report.description = str(item.function.__doc__)
    report.function = item.function.__doc__
    report_directory = os.path.dirname(item.config.option.htmlpath)

    if report.when == 'call' or report.when == "setup":
        extra.append(pytest_html.extras.url(MyConfigFiles.QET_AppURL))
        xfail = hasattr(report, 'wasxfail')
        #print("Xfaile details::", xfail)
        if (report.skipped and xfail) or (report.failed and not xfail):  # or report.outcome:
            #print("Report . Node ID::", report.nodeid)
            file_name = report.nodeid.replace("QA/TestCases/", '\\')
            file_name = file_name.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            extra.append(pytest_html.extras.html('<div>Log description</div>'))
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
                print("Inside IF--HTML", file_name)
            # movfiletodir(file_name)
        report.extra = extra


def _capture_screenshot(name):
    ScreenShot_ReportFile_Path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"TestReport\\")
    MyConfigFiles.driver.get_screenshot_as_file(ScreenShot_ReportFile_Path + name)


@pytest.fixture #(scope='module', autouse=True)
def setup():
    objCommonLib.SelectBrowser(MyConfigFiles.BrowserType)
    MyConfigFiles.driver.implicitly_wait(MyConfigFiles.Implicit_Time_Out)
    MyConfigFiles.driver.get ( MyConfigFiles.QET_AppURL )
    MyConfigFiles.driver.maximize_window()


    yield
    # MyConfigFiles.driver.close()
    # MyConfigFiles.driver.quit()


@pytest.fixture()
def TestData():
    global objDic
    objData = CommonFunctions()
    objDic = objData.readExcelData()
    return objDic


def movfiletodir(file_name):
    PerformActions._createdirectory(MyConfigFiles.ScreenShot_ReportFile_Path + 'Failed')
    shutil.move(MyConfigFiles.ScreenShot_ReportFile_Path + file_name, MyConfigFiles.ScreenShot_ReportFile_Path + 'Failed')










