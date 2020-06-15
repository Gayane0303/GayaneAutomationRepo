import unittest
from selenium import webdriver

from PageObjects.Pages.login_and_logout_page import LoginPage1506
from PageObjects.Pages.main_page import MainPage
from PageObjects.Pages.secure_area_page import SecureAreaPage


class TestLogin1506(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_auth_flow(self):
        main_page = MainPage(self. driver)
        login_page_1506 = LoginPage1506(self.driver)
        secure_area = SecureAreaPage(self.driver)

        main_page.go_login()
        login_page_1506.with_("tomsmith", "SuperSecretPassword!")
        secure_area.button_with_()
        assert login_page_1506.success_message_displayed