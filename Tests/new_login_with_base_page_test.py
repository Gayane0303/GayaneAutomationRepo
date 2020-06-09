import pytest
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as Chrome

from PageObjects.Pages import new_login_page


class TestNewLogin():

    @pytest.fixture()
    def login1(self, request):
        _chromedriver = os.path.join(os.getcwd(), 'drivers', 'chromedriver')
        if os.path.isfile(_chromedriver):
            _service = Chrome(executable_path=_chromedriver)
            driver_ = webdriver.Chrome(service=_service)
        else:
            driver_ = webdriver.Chrome()

        def quit():
            driver_.quit()

        request.addfinalizer(quit)
        return new_login_page.NewLoginPage(driver_)

    def test_valid_credentials(self, login1):
        login1.with_("tomsmith", "SuperSecretPassword!")
        assert login1.success_message_present()

    def test_invalid_credentials(self, login1):
        login1.with_("test", "123456")
        assert login1.fail_message_present()

