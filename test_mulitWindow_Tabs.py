from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

s = Service(ChromeDriverManager().install())
chrome_options = Options()
driver = webdriver.Chrome(service=s, chrome_options=chrome_options)

driver.maximize_window()
driver.get("http://www.theTestingWorld.com/testings")

driver.find_element(By.XPATH, "//label[text()='Login']").click()
driver.find_element(By.NAME,"_txtUserName").send_keys("REMOVED")
driver.find_element(By.NAME,"_txtPassword").send_keys("REMOVED")
driver.find_element(By.XPATH, "//input[@type='submit' and @value='Login']").click()
driver.find_element(By.XPATH, "//a[contains(text(),'My Account')]").click()
driver.find_element(By.XPATH, "//a[contains(text(),'Delete')]").click()

allTabs = driver.window_handles # All the tabs will get a unique value
print(allTabs)
mainWin=""

# You can then loop through the tabs and perform different tasks on different tabs, based on the current_url.
for tab in allTabs:
    driver.switch_to.window(tab)
    print(driver.current_url)
    if(driver.current_url=='http://www.thetestingworld.com/testings/manage_customer.php'):
        driver.find_element(By.XPATH, "//button[text()='Start Download']").click()
        time.sleep(5)
        driver.close()
    elif(driver.current_url=='http://www.thetestingworld.com/testings/dashboard.php'):
         mainWin=win


driver.switch_to.window(mainWin)
print(driver.current_url)

#Note that in some cases the URL of a website is dynamic or changes frequently. If that's the case, you could use driver.title and validate based on that instead.

