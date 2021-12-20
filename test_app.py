

from selenium.webdriver.common.keys import Keys



def test_Login(browser):
    emailTF = browser.find_element_by_accessibility_id('emailTextField')
    emailTF.send_keys("validEmail")
    emailTF.send_keys(Keys.RETURN)
    assert emailTF.get_attribute("value") == "validEmail"
    passwordTF = browser.find_element_by_accessibility_id('passwordTextField')
    passwordTF.send_keys("validPW")
    passwordTF.send_keys(Keys.RETURN)
    print("FFF:"+passwordTF.get_attribute("value"))
    assert passwordTF.get_attribute("value") == '•••••••'
    browser.find_element_by_accessibility_id('loginButton').click()
    smiley = browser.find_element_by_accessibility_id('smileyImage')
    assert str(smiley.get_attribute('wdVisible')) == "true"
    print(str(smiley.get_attribute('wdVisible')))



