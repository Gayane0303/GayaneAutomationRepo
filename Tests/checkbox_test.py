import time
import unittest
from selenium import webdriver

from PageObjects.Pages.checkbox_page import CheckBoxPage
from PageObjects.Pages.main_page import MainPage
from PageObjects.Pages.dropdown_page import DropdownPage


class checkBoxTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_check_first_checkbox(self):
        main_page = MainPage(self.driver)
        main_page.go_checkbox()

        checkbox = CheckBoxPage(self.driver)
        #assert checkbox.is_first_checkbox_checked()

        checkbox.check_first_checkbox()
        time.sleep(3)
        assert checkbox.is_first_checkbox_checked
        assert checkbox.is_second_checkbox_checked

