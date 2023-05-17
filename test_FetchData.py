# pip install webdriver-manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
import time
import pytest

@pytest.fixture()
def environment_setup():
    global driver
    s = Service(ChromeDriverManager().install())
    chrome_options = Options()
    driver = webdriver.Chrome(service=s, chrome_options=chrome_options)

    # This will throw an error if the page doesn't load within 1 second. (By default the timeout is 30 seconds). 1 second often will fail.
    # driver.set_page_load_timeout(1)

    driver.get("http://www.theTestingWorld.com/testings")

    # Maximize browser
    # driver.implicitly_wait(20)
    # driver.maximize_window()

    # This is the maximum timeout -- It asks the program to wait 20 seconds before failing a test. This is to give the page time to load, becuase sometimes certain elements don't exist yet. -- If after 20 seconds the element doesn't exist, then it will fail. -- So if there's code below that the webdriver can't find, it will try, then wait 20 additional seconds, then fail the test if that element still isn't there.
    # See example below. When we select a country from the dropdown, it needs a bit of time to fill the state data, becuase it's based on country. Without this code, the test will fail to find the state. (You could use this implicitely wait or an explicit wait, which is listed in the section).
    # driver.implicitly_wait(20)

    yield
    time.sleep(10) # Pause to allow you to inspect the browser.
    # Close the browser after
    driver.close()

def test_verify_registration(environment_setup):
    #Fetch Data:
    print(driver.title)
    print(driver.current_url)
    print(driver.page_source) # This would fetch the entire page's html.

    print(driver.find_element(By.CLASS_NAME, "displayPopup").text) #This will print out the inner text of the element.

    print(driver.find_element(By.XPATH, '//input[@type="submit"]').get_attribute("value")) #Value of the button

    #  Select an item from a Dropdown (aka select html element with options)
    obj = Select(driver.find_element(By.NAME, "sex"))
    obj.select_by_visible_text("Male")

    # Fetch Selected Option:
    print(obj.first_selected_option.text) # outputs Male

    # This loops through all of the options of the select element, printing out their text (all of the options available in the dropdown, and display the text.)
    for op in obj.options:
        print(op.text)
    # Choose Gender (the placeholder first option), Male and Female are output


    # Work on a Dropdown
    # Explicit wait:
    # You enter which object you want this to work on, and how many seconds.
    wait = WebDriverWait(driver, 100)
    wait.until(ec.text_to_be_present_in_element((By.ID,'countryId'),"India"))

    obj2 = Select(driver.find_element(By.ID, "countryId"))
    obj2.select_by_visible_text("India")
    # After selecting country, it will try to locate the state. But the state isn't automatically there, so it will throw an error as the state field hasn't populated yet (becuase country was just selected, it needs time to get the data.)

    wait.until(ec.text_to_be_present_in_element((By.ID, 'stateId'), "Delhi"))
    obj3 = Select(driver.find_element(By.ID, "stateId"))
    obj3.select_by_visible_text("Delhi")


    # assert driver.current_url == "http://www.theTestingWorld.com/testings"




