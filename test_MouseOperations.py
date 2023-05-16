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

# Click operation
#act.click().perform()
act.click(driver.find_element(By.XPATH, "//label[text()='Login']")).perform()

# Context Click(Right Click)
#act.context_click().perform()
act.context_click(driver.find_element(By.XPATH, "//label[text()='Login']")).perform()

#act.double_click().perform()
act.double_click(driver.find_element(By.XPATH, "//label[text()='Login']")).perform()

# Hover Mouse Over an Element
act.move_to_element(driver.find_element(By.XPATH, "//label[text()='Register']")).perform()


time.sleep(10) # Pause to allow you to inspect the browser.

driver.quit()

# This was just to keep the browser open:
# input()



