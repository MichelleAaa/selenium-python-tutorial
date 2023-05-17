
def take_page_screenshot(driver, name):
    driver.get_screenshot_as_file('C:/Users/myPathHere/PycharmProjects/pythonProject/' + name + '.png')