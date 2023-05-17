# pip install webdriver-manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pytest

a = 100

#Fixtures allow you to run code before or after the test cases.
@pytest.fixture(scope="module")
def initiate_driver():
    #when you add scope="module", the code in this file will only execute once. That means that only one browser window will open, then all the test cases will be executed in that one browser, and then it will get to the yield section and close that one browser at the end of all the tests.
    # Without including scope="module" one browser each would open and close for each test.
    # global will allow driver to be used outside of the function.
    global driver
    s = Service(ChromeDriverManager().install())
    chrome_options = Options()
    driver = webdriver.Chrome(service=s, chrome_options=chrome_options)
    yield
    driver.close()
#     whatever you write after yield will run AFTER all of the test cases. (Whatever is written before yield (or if yield isn't listed) will be ran BEFORE the test cases.


# This asks pytest to skip this test
# @pytest.mark.skip("Don't want to execute on current build.")
# @pytest.mark.skipif(a > 100, reason = "Don't want to execute on current build.")
# Smoke is the name of a group:
@pytest.mark.Smoke
def test_registration_valid_data(initiate_driver):
    driver.get("http://www.theTestingWorld.com/testings")
    driver.maximize_window()
    assert driver.title == "Login & Sign Up Forms"

@pytest.mark.Sanity
def test_registration_invalid_data(initiate_driver):
    driver.get("http://www.theTestingWorld.com/testings")
    driver.maximize_window()
    assert driver.current_url == "http://www.theTestingWorld.com/testings/register.php"

@pytest.mark.Smoke
def test_invalid_data(initiate_driver):
    driver.get("http://www.theTestingWorld.com/testings")
    driver.maximize_window()

# Terminal Commands:
# This can be executed by typing pytest in the terminal after navigating to the folder.
#pytest -v : v is for verbose, it will give more details in the terminal.

#Run only one file:
    #pytest tst_file_name.py

#Execute a specific testcase only:
    # pytest -k test_registration_invalid_data

#Execute a group of tests (which are labeled @pytest.mark.MadeUpGroupNameHere):
    # pytest -m Smoke
    # You can also go with verbose mode:
    # pytest -m Smoke -v

# Run all test cases except one group (group again is marked with @pytest.mark.MadeUpGroupNameHere)
    # pytest -m "not Sanity" -v


# Note that when it says deselected, it means how many functions were not ran from the file because they didn't meet the conditions you specified.

