import time
import unittest
from selenium import webdriver

from PageObjects.Pages.main_page import MainPage
from PageObjects.Pages.dropdown_page import DropdownPage


class dropdown(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_dropdown(self):
        main_page = MainPage(self.driver)
        main_page.go_dropdown()

        dropdown = DropdownPage(self.driver)
        dropdown.click_on_dropdown()
        dropdown.selectDropdownListItem()
        assert dropdown.is_slected_item_displayed
        #time.sleep(2)

    def test_get_dropdown_item_list(self):
        main_page = MainPage(self.driver)
        main_page.go_dropdown()

        dropdown = DropdownPage(self.driver)
        dropdown.click_on_dropdown()
        dropdown.getDropdownItemsList()
        dropdown.click_on_dropdown()

        self.assertEqual(("Please select an option", "Option 1", "Option 2"), dropdown.getDropdownItemsList())


