from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# @pytest.fixture()
# def environment_setup():
#     global driver
s = Service(ChromeDriverManager().install())
chrome_options = Options()
driver = webdriver.Chrome(service=s, chrome_options=chrome_options)

driver.maximize_window()
driver.get("http://toolsqa.com/iframe-practice-page/")
# driver.switch_to.frame("iframe2") #this website's not working, but in the lesson there's an iframe html element on this page. -- iframe2 is the name tag on the element.
#if you want to use the ID instead of the name, you could reference that as well. There's no need to indicate:
driver.switch_to.frame("IF2")
# If you want to use an XPATh, you would need to use the driver.dinf_element(By.XPATH .... syntax as a parameter of frame().
driver.find_element(By.XPATH, "//a[contains(text(), 'Read more')]").click()

# Becuase the control is in the iframe, you can't target elements outside of the iframe until you switch back to the main content.
# This will go back to the main content:
driver.switch_to.default_content()


