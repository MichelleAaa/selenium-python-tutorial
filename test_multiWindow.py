from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.fixture()
def environment_setup():
    global driver
    s = Service(ChromeDriverManager().install())
    chrome_options = Options()
    driver = webdriver.Chrome(service=s, chrome_options=chrome_options)

    driver.get("http://www.theTestingWorld.com/testings")

    driver.maximize_window()
    yield
    time.sleep(10) # Pause to allow you to inspect the browser.
    # Close the browser after
    driver.close()

def test_verify_registration(environment_setup):
    driver.find_element(By.XPATH, "//label[text()='Login']").click()
    driver.find_element(By.NAME, '__txtUserName').send_keys("REDACTED")
    driver.find_element(By.NAME, '__txtPassword').send_keys("REDACTED")
    driver.find_element(By.XPATH, "//input[@type='submit' and @value='Login']").click()
    driver.find_element(By.XPATH, "//a[contains(text(), 'My Account')]").click()
    driver.find_element(By.XPATH, "//a[contains(text(), 'Update')]").click()
    # When you click update it opens a new tab.

    allwindows = driver.window_handles
    print(allwindows)

    mainWin = ""

    for win in allwindows:
        driver.switch_to.window(win)
        print(driver.current_url)
        if(driver.current_url = 'http://www.theTestingWorld.com/testings/manage_customer.php'):
            driver.find_element((By.XPATH, "//button[text()='StartDownload']")).click()
            time.sleep(5)
            driver.close()
        elif (driver.current_url = 'http://www.theTestingWorld.com/testings/dashboard.php'):
            mainWin = win

        driver.switch_to.window(mainWin)
        driver.current_url
