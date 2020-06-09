from selenium.webdriver.common.by import By

from PageObjects.Pages.base_page import BasePage


class NewLoginPage(BasePage):
    _username_input = {"by": By.ID, "value": "username"}
    _password_input = {"by": By.ID, "value": "password"}
    _login_button = {"by": By.CSS_SELECTOR, 'value': "button"}
    _success_message = {"by": By.CSS_SELECTOR, "value": ".flash.success"}
    _fail_message = {"by": By.CSS_SELECTOR, "value": ".flash.error"}


    def __init__ (self, driver):
        self.driver = driver
        #driver.maximize_window()
        self._visit("https://the-internet.herokuapp.com/login")

    def with_(self, username, password):
        self.driver.find_element(self._username_input["by"],
                                 self._username_input["value"]).send_keys(username)
        self.driver.find_element(self._password_input["by"],
                                 self._password_input["value"]).send_keys(password)
        self.driver.find_element(self._login_button["by"],
                                 self._login_button["value"]).click()

    def success_message_present(self):
        return self.driver.find_element(
            self._success_message["by"],self._success_message["value"]).is_displayed()


    def fail_message_present(self):
        return self.driver.find_element(
            self._fail_message["by"],self._fail_message["value"]).is_displayed()
