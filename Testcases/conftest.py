from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        print("Launching Chrome Browser .......")
        driver = webdriver.Chrome(executable_path='C:\seleniumdrivers\chromedriver.exe')

    elif browser == 'firefox':
        print("Launching Firefox browser......")
        capabilities = webdriver.DesiredCapabilities().FIREFOX
        capabilities["marionette"] = False
        # browser = webdriver.Firefox(capabilities=capabilities)
        driver = webdriver.Firefox(executable_path='C:\seleniumdrivers\geckodriver.exe', capabilities=capabilities)
        #driver = webdriver.Chrome(executable_path='C:\seleniumdrivers\geckodriver.exe')
        print("Launching Firefox browser")
    else:
        print("Launching default browser")
        driver = webdriver.Edge(executable_path='C:\Program Files\Internet Explorer\ExtExport.exe')
    return driver

#def setup():
    #driver = webdriver.Chrome()
    #chrome_options = webdriver.ChromeOptions()
 #   capabilities = webdriver.DesiredCapabilities().FIREFOX
  #  capabilities["marionette"] = False
    #browser = webdriver.Firefox(capabilities=capabilities)
   # driver = webdriver.Firefox(executable_path='C:\seleniumdrivers\geckodriver.exe',capabilities=capabilities)
        #chrome_options=chrome_options)
    #return driver
def pytest_addoption(parser): # this will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #This will resturn the browser value to setup method
    return request.config.getoption("--browser")

##### Pytest html report ##

def pytest_configure(config):
    config._metadata['Project Name'] = 'nopommerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Veni'

# Cook to delete/modify Environment info to HTML report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)
