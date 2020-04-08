from QA.PageObjects.Test_Locators import PCN
from QA.Utilities.PerformAction import PerformActions
from QA.Utilities.CommonLib import CommonFunctions
from QA.Base.Config import MyConfigFiles
from QA.BusinessLogic.Home_Page import Home
from QA.BusinessLogic.Filter_Page import Filter
from QA.BusinessLogic.CreateJPCN_Page import createJPCN_Page
from QA.BusinessLogic.InitialAssessment_Page import InitilaAssessment_Page
from QA.Base.Config import MyConfigFiles
import mysql.connector
from mysql.connector import Error
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from pathlib import Path
import sys
import time

class mySql_Connections():
    global objCommon, objActions, objConfig,objHome,objFilter,objCreateJPCN,objInitialAssessment
    objCommon = CommonFunctions()
    objActions = PerformActions()
    objConfig=MyConfigFiles()
    objFilter=Filter()
    objHome=Home()
    objCreateJPCN = createJPCN_Page()
    objInitialAssessment =InitilaAssessment_Page()

    def DB_Connections_execute(self,db_host,db_username,db_password,UserName,strResponsibleCoreCE,pcnid):
        try:
            # mydb=mysql.connector.connect(host=MyConfigFiles.db_host, user=MyConfigFiles.db_username, passwd=MyConfigFiles.db_password)
            mydb = mysql.connector.connect(host=db_host, user=db_username, passwd=db_password)
            mydb.autocommit = False
            mycursor=mydb.cursor()
            strQuery = "update tpcn.tb_jpn_details set commodity_mgr='"+UserName+"',commodity_mgr_name='"+strResponsibleCoreCE+"' where pcn_id='"+pcnid+"' and commodity_group='Voltage Regulator'"
            print('Query: '+strQuery)
            mycursor.execute(strQuery)#show databases
            mydb.commit()
            print("Record Updated successfully")
        except Exception:
            print('error message:')
        # for i in mycursor:
        #     print(i)#UserName,strResponsibleCoreCE,