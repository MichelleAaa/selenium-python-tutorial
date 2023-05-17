from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import logging


s = Service(ChromeDriverManager().install())
chrome_options = Options()
driver = webdriver.Chrome(service=s, chrome_options=chrome_options)

# Create a logger object
log = logging.getLogger(__name__) #__name__ is a default function
# Then we have to set the level of the log
log.setLevel(logging.DEBUG)

# Set where you want to save the files:
warn = logging.FileHandler('Warning_logs.txt') #This indicates that it should be saved in the current directory.
warn.setLevel(logging.WARNING)

info = logging.FileHandler('Info_logs.txt')
info.setLevel(logging.INFO)

# Set the formatting of the logs
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#on the logs we specified above, we are setting the format as formatter
warn.setFormatter(formatter)
info.setFormatter(formatter)


driver.maximize_window()
driver.get("http://www.theTestingWorld.com/testings")

# These print to the browser:
log.info("[ My URL is Opened]")
log.warning("[There is a delay in the opening of the browser]")