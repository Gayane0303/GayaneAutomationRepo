from selenium.webdriver.common.by import By
from PageObjects.Pages.base_page import BasePage

class MainPage(BasePage):
    _login_link= {"by": By.LINK_TEXT, "value": "Form Authentication"}
    _dropdown_link = {"by": By.LINK_TEXT, "value": "Dropdown"}
    _checkbox_link = {"by": By.LINK_TEXT, "value": "Checkboxes"}


    def __init__(self, driver):
        self.driver = driver
        driver.maximize_window()
        self._visit("https://the-internet.herokuapp.com")

    def go_login(self):
        self._click(self. _login_link)

    def go_dropdown(self):
        self._click(self._dropdown_link)

    def go_checkbox(self):
        self._click(self._checkbox_link)