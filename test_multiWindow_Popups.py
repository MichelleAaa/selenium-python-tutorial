from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


s = Service(ChromeDriverManager().install())
chrome_options = Options()
driver = webdriver.Chrome(service=s, chrome_options=chrome_options)

driver.maximize_window()
driver.get("http://www.theTestingWorld.com/testings")

allwindows = driver.window_handles #This will print all the different window handlers, which are assigned to the different tabs and popups.
print(allwindows) # note that you need to open this with python, not pytest, for it to print.

#   HANDLE POPUPS
#You could use a for loop to loop through all of the ID's of the tabs/pages/popup windows -- then you could use if/else to execute code on the page you want to work on, and to close the popups and other tabs. -- On this website there's no popups but it's included as an example:
mainWin=""
for win in allwindows:
    driver.switch_to.window(win) # Here we are switching to the window with the ID provided by the array from driver.window_handles.
    print(driver.current_url)
    if(driver.current_url=='http://www.thetestingworld.com/testings'):
        mainWin = win
    else:
        driver.close()
# After you go through and close the popup windows, you can then switch back to your main window.
driver.switch_to.window(mainWin)
print(driver.current_url)