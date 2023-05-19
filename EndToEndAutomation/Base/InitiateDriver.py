from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from Library import ConfigReader

def startBrowser():
    global driver

    if ((ConfigReader.readConfigData('Details', 'Browser')) == 'chrome'):
        s = Service(ChromeDriverManager().install())
        chrome_options = Options()
        driver = webdriver.Chrome(service=s, chrome_options=chrome_options)
    elif ((ConfigReader.readConfigData('Details', 'Browser')) == 'firefox'):
        driver = webdriver.Firefox()
    else:
        s = Service(ChromeDriverManager().install())
        chrome_options = Options()
        driver = webdriver.Chrome(service=s, chrome_options=chrome_options)

    # driver.get("http://www.theTestingWorld.com/testings")
    # Section Details, Key Application_URL:
    driver.get(ConfigReader.readConfigData('Details', 'Application_URL'))
    driver.maximize_window()
    return driver

def closeBrowser():
    driver.close()