from Base import InitiateDriver
from Pages import RegistrationPage
from DataGenerate import DataGen
import pytest

#Here we are getting the function that loops through the excel workbook data from the DataGen file. The test case below is run as many times as there's data in the file.

# First param is the name of the data, which you can make up. the second is where the data is coming from.
# dataGenerator executes, and sends each to the below function, one at a time. So we pass in data, and then access the indexes of the inner lists.
@pytest.mark.parametrize('data', DataGen.dataGenerator())
def test_registration_invalid_data(data):
    driver = InitiateDriver.startBrowser()
    register = RegistrationPage.Registration(driver) #Creates an object of the Registration class
    register.enter_username(data[0])
    register.enter_password(data[1])
    InitiateDriver.closeBrowser()


