# pip install webdriver-manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import TakeScreenshot

s = Service(ChromeDriverManager().install())
chrome_options = Options()
driver = webdriver.Chrome(service=s, chrome_options=chrome_options)

driver.maximize_window()
driver.get("http://www.theTestingWorld.com/testings")
# Here we are asking selenium to take a screenshot, and we are giving the full path with file name for where it should be stored.
# driver.get_screenshot_as_file('C:/Users/psi33/PycharmProjects/pythonProject/BeforeRegistration.png')

# Another option is to just create a separate function for taking screenshots and invoke it, since you will likely need to take a lot of screenshots.
TakeScreenshot.take_page_screenshot(driver, "First_Screenshot")