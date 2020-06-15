import pytest
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as Chrome

from PageObjects.Pages import login_page
from PageObjects.Pages.login_page import LoginPage
from PageObjects.Pages.main_page import MainPage
from PageObjects.Pages.secure_area_page import SecureAreaPage


class TestLogin():
    @pytest.fixture()
    def login(self, request):
        _chromedriver = os.path.join(os.getcwd(), 'drivers', 'chromedriver')
        if os.path.isfile(_chromedriver):
            _service = Chrome(executable_path=_chromedriver)
            driver_ = webdriver.Chrome(service=_service)
        else:
            driver_ = webdriver.Chrome()

        def quit():
            driver_.quit()

        request.addfinalizer(quit)
        return login_page.LoginPage(driver_)

    def test_valid_credentials(self, login):
        login.with_("tomsmith", "SuperSecretPassword!")
        assert login.success_message_present()

    def test_invalid_credentials(self, login):
        login.with_("test", "123456")
        assert login.fail_message_present()


