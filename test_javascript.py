# pip install webdriver-manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

s = Service(ChromeDriverManager().install())
chrome_options = Options()
driver = webdriver.Chrome(service=s, chrome_options=chrome_options)

driver.maximize_window()
driver.get("http://www.theTestingWorld.com/testings")
# execute_script will execute JavaScript.
# 0 = horizontal, 400 = vertical pixels
# Here we are executing code to scroll down the page. The reason is that some websites don't load until you scroll down to the content, so sometimes you will need to add this.
driver.execute_script("window.scrollTo(0, 400);")
# Note that if you have more lines of js, you would just end each with a ;