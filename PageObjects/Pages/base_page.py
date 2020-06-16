from selenium.common.exceptions import NoSuchElementException,TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    def __init__ (self, driver):
        self.driver = driver

    def _visit(self, url):
        self.driver.get(url)

    def _find(self, locator):
        return self.driver.find_element(locator['by'], locator['value'])

    def _click(self, locator):
        self._find(locator).click()

    def _type_text(self, locator, input_test):
        self._find(locator).send_keys(input_test)

    def _is_displayed(self, locator):
        self._find(locator).is_displayed()

    #def _click(self, locator):
        #self._find(locator).click()

    def _is_checked(self, locator):
        self._find(locator).is_selected()

    def _is_checkbox_checked(self, locator):
        return self._find(locator).get_attribute("checked")

    def _is_checkbox_selected(self, locator):
        return self._find(locator).is_selected()

