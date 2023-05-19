from Base import InitiateDriver
from selenium.webdriver.common.by import By
from Library import ConfigReader

def test_ValidateRegistration():
    driver = InitiateDriver.startBrowser()
    driver.find_element(By.NAME, (ConfigReader.fetchElementLocators("Registration", "password_name"))).send_keys("Hello")
    InitiateDriver.closeBroser()


