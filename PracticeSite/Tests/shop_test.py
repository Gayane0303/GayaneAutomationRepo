from selenium.webdriver import Chrome
import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class TestShop():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://automationpractice.com/index.php")
        yield
        driver.close()
        driver.quit()
        print("PASS")

    def test_item(self, test_setup):
        elementBeforeClick=driver.find_element_by_xpath('//*[@id="homefeatured"]/li[1]/div/div[2]/h5/a')
        action = ActionChains(driver);
        action.move_to_element(elementBeforeClick).perform();
        driver.execute_script("arguments[0].scrollIntoView();", elementBeforeClick)
        elementTextBefore=elementBeforeClick.__getattribute__('text')
        print(elementTextBefore)
        elementBeforeClick.click()
        elementTextAfter=driver.find_element_by_xpath('//div[3]/h1').__getattribute__('text')
        print(elementTextAfter)
        assert elementTextBefore == elementTextAfter


