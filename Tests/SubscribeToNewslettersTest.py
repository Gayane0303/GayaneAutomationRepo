from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from PageObjects.Pages.RandomDataPageObject import randomString
from PageObjects.Pages.SubscribeToNewslettersPageObjects import Home

with Chrome() as driver:
    driver.maximize_window()
    driver.get("https://www.etsy.com/")
    home = Home(driver)
    subscribeToNewslettersInputField=driver.find_element_by_xpath('//*[@id="email-list-signup-email-input"]')
    driver.execute_script("arguments[0].scrollIntoView();", subscribeToNewslettersInputField)
    subscribeToNewslettersInputField.click()
    subscribtionEmail=subscribeToNewslettersInputField.send_keys(randomString()+"@mailinator.com")
    wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_all_elements_located((By.XPATH,'//*[@id="email-list-signup-email-input"]')))
    attValue=subscribeToNewslettersInputField.get_attribute('textcontent')
    assert attValue==subscribtionEmail
    home.subscribeButton().click()
    wait.until(ec.visibility_of_all_elements_located((By.XPATH,'//div/form/div[3]/div[5]')))
    assert driver.find_element_by_xpath('//div/form/div[3]/div[5]').is_displayed()


