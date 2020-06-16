from selenium.webdriver.common.by import By
import time
from PageObjects.Pages.base_page import BasePage
from selenium.webdriver.support.ui import Select



class DropdownPage(BasePage):
    _dropdown = {"by": By.ID, "value": "dropdown"}
    _dropdownItem1 = {"by": By.XPATH, "value": "//*[@id='dropdown']/option[2]"}
    _items = {"by": By.XPATH, "value": "//*[@id='dropdown']/option"}

    def __init__(self, driver):
        self.driver = driver

    def click_on_dropdown(self):
        self._click(self._dropdown)

    def is_slected_item_displayed(self):
        self._is_displayed(self._dropdownItem1)

    def selectDropdownListItem(self):
        getDropdownItem1 = self.driver.find_element(self._dropdown["by"],
                                                    self._dropdown["value"])
        item1 = Select(getDropdownItem1)
        item1.select_by_visible_text("Option 1")
        #item1.select_by_index(1)

    def getDropdownItemsList(self):
        getDropdownItemsList = self.driver.find_elements(self._dropdown["by"],
                                                         self._dropdown["value"])
        for i in getDropdownItemsList:
            print(i.text)
        print(getDropdownItemsList)


