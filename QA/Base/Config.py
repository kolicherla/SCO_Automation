class MyConfigFiles():
     global driver
     BrowserType='gc' #GC or GOOGLE CHROME- for googlechrome,    FF or FIREFOX for firefox    IE or INTERNET EXPLORER for internet explorer
     Environment='local' # local- to execute on windows system,   remote- to execute on linux remote server
     Implicit_Time_Out = 10  #decides the timeout of the entire framework
     AppURL="https://www.google.com" #URL of the application under test
     App_Title = "Google"  # title of the application displayed
#pcn-test.sndbx.junipercloud.net