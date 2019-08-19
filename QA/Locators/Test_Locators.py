class MyJuniperLocators():

#QET Login page objects
    username_textbox_id = "userid"
    password_textbox_id = "password"
    submit_button_xpath = "//button[@type='submit']"

#QET Home Page
    SCARs_link_xpath = "//a[text()='SCARs']"

#SCAR Home page
    Create_button_xpath = "//button[@class='success margin-right-small']"
    ProblemDescription_WebEdit_xpath="//legend[contains(text(),'Problem Description')]/..//textarea"
    AffectedPart_webEdit_xpath="(//th[text()='Affected Part']/../../../..//input[@data-id='0'])[1]"
    AffectedPart_DropDown_xpath="'//li[@data-part='+TestData['AffectedPart']'"      #dynamic
    UserGroup_SelectBox_xpath="(//select)[1]"
    Supplier_SelectBox_xpath="(//select)[2]"
    Contact_SelectBox_xpath="//select[@class='margin-bottom' and @data-type='contact']"
    Escalation_SelectBox_xpath="//select[@class='margin-bottom' and @data-type='escalation']"
    Escalation_WebEdit_xpath="//input[@name='escaList']"
    SupplierWatchList_WebEdit_xpath="//select[@class='margin-bottom' and @data-type='watchlist']"
    CreateScar_button_xpath="//button[@class='success']"




