from selenium.webdriver.common.by import By
import time
from PageObjects.Pages.base_page import BasePage
from selenium.webdriver.support.ui import Select



class DropdownPage(BasePage):
    _dropdown = {"by": By.ID, "value": "dropdown"}
    _dropdownItem1 = {"by": By.XPATH, "value": "//*[@id='dropdown']/option[2]"}

    def __init__(self, driver):
        self.driver = driver
        driver.maximize_window()
        self._visit("https://the-internet.herokuapp.com/dropdown")

    def clickOnDropDown(self):
        self.driver.find_element(self._dropdown["by"],
                                 self._dropdown["value"]).click()

    def getDropdownList(self):
        dropdownList = self.driver.find_element(self._dropdown["by"],
                                                self._dropdown["value"]).text
        print(dropdownList)

    def selectDropdownListItem(self):
        getDropdownItem1 = self.driver.find_element(self._dropdown["by"],
                                                   self._dropdown["value"])
        item1=Select(getDropdownItem1)
        item1.select_by_visible_text("Option 1")

    def getDropdownItemText(self):
        getDropdownItem1 = self.driver.find_elements(self._dropdown["by"],
                                                    self._dropdown["value"])
        for i in getDropdownItem1:
            print(i.text)
        print(getDropdownItem1)
