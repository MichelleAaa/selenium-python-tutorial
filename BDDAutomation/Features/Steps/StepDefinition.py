# from behave import given
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

#note that the browser is started in environment.py in the before_all() statement. All test cases will run on the same browser, and at the end, the browser will close with the after_all() function.

@given(u'User is on Registration page')
def step_impl(context):
    context.driver.get("http://www.theTestingWorld.com/testings")

@when(u'User enters username')
def step_impl(context):
    context.driver.find_element(By.NAME, "fld_username").send_keys("helloworld")


@when(u'User enters email id')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@name='fld_email']").send_keys("testingworldindia@gmail.com")


@when(u'User enters password')
def step_impl(context):
    context.driver.find_element(By.NAME, "fld_password").send_keys("abcd123")


@when(u'User clicks on signup button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@type='submit']").click()


@then(u'User should be registered successfully')
def step_impl(context):
    # This is just a placeholder:
    print("Registered")


@when(u'User enters a duplicate username')
def step_impl(context):
    # This is just a placeholder
    print("Not registered")
