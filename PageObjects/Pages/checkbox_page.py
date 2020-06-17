from selenium.webdriver.common.by import By
import time
from PageObjects.Pages.base_page import BasePage

class CheckBoxPage(BasePage):
    _first_checkbox = {"by": By.XPATH, "value": "//*[@id='checkboxes']/input[1]"}
    _second_checkbox = {"by": By.XPATH, "value": "//*[@id='checkboxes']/input[2]"}

    def __init__(self, driver):
        self.driver = driver

    def check_first_checkbox(self):
        self._click(self._first_checkbox)

    def is_first_checkbox_checked(self):
        return self._is_checkbox_selected(self._first_checkbox)

    def is_second_checkbox_checked(self):
        return self._is_checkbox_selected(self._second_checkbox)

