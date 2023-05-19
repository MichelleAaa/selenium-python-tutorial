from Base import InitiateDriver
from Pages import RegistrationPage

def test_registration_invalid_data():
    driver = InitiateDriver.startBrowser()
    register = RegistrationPage.Registration(driver) #Creates an object of the Registration class
    register.enter_username('hello')
    register.enter_password('abcd')
    InitiateDriver.closeBrowser()


