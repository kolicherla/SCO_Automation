

class MyJuniperLocators():
    #MyJuniper Landing page Objects
    landingPage_Logo_xPath= "//a[@id='logoHolder']"
    create_New_Account_xPath = "//a[contains (text(),'New Account')]"

    #New Account Setup page
    newUser_eMail_xPath="//input[@name='email']"
    reEnterNewUser_eMail_xPath="// input[ @ name = 'reEnteredEmail']"
    countryDropDown_xPath="//select[@name='selectedCountry']"
    clickNextBtn_xPath="//input[@value='Next>']"

    #QET Login page objects
    username_textbox_id = "userid"
    password_textbox_id = "password"
    submit_button_id = "submit"

    # QET Home page
    SRNum_link_linktext = "SQ00002"
    BackToOpportunitites_link_linktext = "Back to all opportunities"
    QualTracker_link_linktext="Qual Tracker"
    createOpportunity_btn_xpath="//button[@class='success']"
    pcndesign_button_xpath="//span[@title='Product Change Notice - Design']"
    NewSupplier_webedit_xpath="//input[@name='supplier']"
    NewMPin_webedit_xpath="//input[@name='newMPN']"
    SupplierPCN_webedit_xpath="//input[@name='supplierPcn']"
    Cancel_btn_xpath="//a[@class='button danger margin-right-small']"
    Logout_link_linktext = "Logout"

