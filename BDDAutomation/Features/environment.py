from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Whatever you have defined as context can be used throughout the project.
def before_all(context):
    s = Service(ChromeDriverManager().install())
    chrome_options = Options()
    # If you create driver as a context variable, then
    context.driver = webdriver.Chrome(service=s, chrome_options=chrome_options)

def after_all(context):
    context.driver.close()

# ANOTHER OPTION:
#if you prefer, you could use this setup. (This would be if you had multiple feature files).
# def before_feature(context, feature):
#     s = Service(ChromeDriverManager().install())
#     chrome_options = Options()
#     # If you create driver as a context variable, then
#     context.driver = webdriver.Chrome(service=s, chrome_options=chrome_options)
#
# def after_feature(context, feature):
#     context.driver.close()


# ANOTHER OPTION:
# The browser would start, first scenario would run, then it would close. Then repeat. The top one would only open the browser once and close it once at the end.
# def before_scenario(context, scenario):
#     s = Service(ChromeDriverManager().install())
#     chrome_options = Options()
#     # If you create driver as a context variable, then
#     context.driver = webdriver.Chrome(service=s, chrome_options=chrome_options)
#
# def after_scenario(context, scenario):
#     context.driver.close()


# Some other options:
# def before_tag(context, tag):
# def before_step(context, step):