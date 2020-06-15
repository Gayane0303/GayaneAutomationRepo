import pytest
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as Chrome

from PageObjects.Pages import dropdown_page
from selenium import webdriver


class TestDropdown():
    @pytest.fixture()
    def dropdown(self, request):
        _chromedriver = os.path.join(os.getcwd(), 'drivers', 'chromedriver')
        if os.path.isfile(_chromedriver):
            _service = Chrome(executable_path=_chromedriver)
            driver_ = webdriver.Chrome(service=_service)
        else:
            driver_ = webdriver.Chrome()

        def quit():
            driver_.quit()

        request.addfinalizer(quit)
        return dropdown_page.DropdownPage(driver_)

    def test_dropdown(self, dropdown):
        dropdown.clickOnDropDown()
        dropdown.selectDropdownListItem()
        #assert dropdown.getDropdownItemText(1)=="Option 1"

        #assert dropdown.getDropdownList()=="Option 1", "Option 2"



