import configparser

# Section is in [] in the .cfg file, while key is the key pair.
def readConfigData(section, key):
    config = configparser.ConfigParser()
    # config.read("../Configuration/config.cfg")
    config.read('C:\\Users\\UPDATE\\PycharmProjects\\pythonProject\\EndToEndAutomation\\Configuration\\config.cfg')
    return config.get(section, key)

# print(readConfigData('Details', "Application_URL"))

def fetchElementLocators(section, key):
    config = configparser.ConfigParser()
    # config.read("../Configuration/Elements.cfg")
    config.read("C:\\Users\\UPDATE\\PycharmProjects\\pythonProject\\EndToEndAutomation\\Configuration\\Elements.cfg")
    return config.get(section, key)

