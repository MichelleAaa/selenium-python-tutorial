# pip install webdriver-manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select


s = Service(ChromeDriverManager().install())
chrome_options = Options()
driver = webdriver.Chrome(service=s, chrome_options=chrome_options)


driver.get("http://www.theTestingWorld.com/testings")

# Maximize browser

driver.maximize_window()



#  Enter Data in the textbox
# send_keys is the method for entering text into an input.
#  https://selenium-python.readthedocs.io/locating-elements.html
driver.find_element(By.XPATH, "//input[@name='fld_email']").send_keys("testingworldindia@gmail.com")
driver.find_element(By.NAME, "fld_username").send_keys("helloworld")
driver.find_element(By.NAME, "fld_password").send_keys("abcd123")
driver.find_element(By.NAME, "fld_cpassword").send_keys("abcd123")
driver.find_element(By.NAME, "fld_username").clear()
# We had to use the above line to clear the text content in fld_username, because we entered content in there first.
# If you don't, then the new text will be appended to the previous text.
driver.find_element(By.NAME, "fld_username").send_keys("abcd123")

# Clicking on Radio button
driver.find_element(By.XPATH, "//input[@value='office']").click()

#  Select an item from a Dropdown (aka select html element with options)
#  https://selenium-python.readthedocs.io/navigating.html
obj = Select(driver.find_element(By.NAME, "sex")) # You have to create an object when working with a select.
# Some options for selecting options from the dropdown:
obj.select_by_visible_text("Male")
obj.select_by_value("2")
obj.select_by_index(2)

# On a list, you have an option to deselect as well. Because lists allow you to select more than one value, while the dropdown only allows one.

# Click on Checkbox
driver.find_element(By.NAME, "terms").click()

# Click on Button
driver.find_element(By.XPATH, "//input[@type='submit']").click()

# Click on link
driver.find_element(By.LINK_TEXT, "Read Detail").click()

# Close the browser
driver.close()

# Instructions are old. This was used before driver.close() was added is just to keep the browser open. (it was auto-closing.)
# input()