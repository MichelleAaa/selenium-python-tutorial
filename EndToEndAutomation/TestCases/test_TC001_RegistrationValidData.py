from Base import InitiateDriver
from Pages import RegistrationPage
import pytest

def dataGenerator():
    li = [['uname1', 'pass1'], ['uname2', 'pass3'], ['uname3', 'pass3']]
    return li

# First param is the name of the data, which you can make up. the second is where the data is coming from.
# dataGenerator executes, and sends each to the below function, one at a time. So we pass in data, and then access the indexes of the inner lists.
@pytest.mark.parametrize('data', dataGenerator())
def test_registration_invalid_data(data):
    driver = InitiateDriver.startBrowser()
    register = RegistrationPage.Registration(driver) #Creates an object of the Registration class
    register.enter_username(data[0])
    register.enter_password(data[1])
    InitiateDriver.closeBrowser()


