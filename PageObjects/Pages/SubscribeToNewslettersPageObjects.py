from selenium.webdriver.common.by import By
from PageObjects.Locators import Locator


class Home(object):
    def __init__(self, driver):
        self.driver=driver

        self.subscribeToNewslettersButton=driver.find_element(By.XPATH, Locator.subscribeToNewslettersButton)

    def subscribeButton(self):
        return self.subscribeToNewslettersButton

    def subscribeToNewslettersInputField(self):
        return self.subscribeToNewsLettersInputField

    #def clickOnSubscribeButton(self,subscribeButton):
    #    subscribeButton.click()



