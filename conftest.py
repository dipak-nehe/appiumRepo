import pytest
import appium.webdriver
from appium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    app = '/Users/dipaknehe/Library/Developer/Xcode/DerivedData/AppiumTest-hiayiqvgveiykhcmqnyswuszzeuj/build/Products/Debug-iphonesimulator/AppiumTest.app'
    driver = appium.webdriver.Remote(
        command_executor='http://127.0.0.1:4723/wd/hub',
        desired_capabilities={
            'app': app,
            'platformName': 'iOS',
            'platformVersion': '15.2',
            'deviceName': 'iPhone 11'
        }
    )

    options = Options()

    # return driver instance for set up
    yield driver

    # quit the webdriver instance for the clean
    driver.quit()