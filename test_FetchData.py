# pip install webdriver-manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.wait import WebDriverWait

import time

s = Service(ChromeDriverManager().install())
chrome_options = Options()
driver = webdriver.Chrome(service=s, chrome_options=chrome_options)


driver.get("http://www.theTestingWorld.com/testings")


# Maximize browser
# driver.implicitly_wait(20)
# driver.maximize_window()

#Fetch Data:
print(driver.title)
print(driver.current_url)
print(driver.page_source) # This would fetch the entire page's html.

# yield
# driver.close()
#
#
# #  Work on Dropdown
# wait  = WebDriverWait(driver,100)
# wait.until(ec.text_to_be_present_in_element((By.ID,'countryId'),"India"))
# obj = Select(driver.find_element(By.ID,"countryId"))
#
# obj.select_by_visible_text("India")
#
# wait.until(ec.text_to_be_present_in_element((By.ID, 'stateId'), "Delhi"))
# obj = Select(driver.find_element(By.ID, "stateId"))
# obj.select_by_visible_text("Delhi")


time.sleep(10) # Pause to allow you to inspect the browser.

# Close the browser
driver.close()

