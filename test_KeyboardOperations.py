# pip install webdriver-manager
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

s = Service(ChromeDriverManager().install())
chrome_options = Options()
driver = webdriver.Chrome(service=s, chrome_options=chrome_options)


driver.get("http://www.theTestingWorld.com/testings")
driver.find_element(By.NAME, "fld_username").send_keys("Hello")

act = ActionChains(driver) # this ensures that the actions are performed on the same browser/tab that we just created.
act.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).perform()

act.send_keys(Keys.TAB).perform()

time.sleep(10) # Pause to allow you to inspect the browser.

driver.quit()

# This was just to keep the browser open:
# input()
