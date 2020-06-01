from selenium import webdriver
import unittest

class SignIn(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get('http://automationpractice.com/index.php')

    def test_login_invalid(self):
        self.driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/nav/div[1]/a').click()
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys('test@mailinator.com')
        self.driver.find_element_by_xpath('//*[@id="passwd"]').send_keys('123456')
        self.driver.find_element_by_xpath('//*[@id="SubmitLogin"]/span').click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('PASSED')