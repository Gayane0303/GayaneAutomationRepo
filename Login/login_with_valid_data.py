import ec as ec
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

with Chrome() as driver:
    driver.maximize_window()
    driver.get("http://the-internet.herokuapp.com/login")
    driver.find_element_by_id("username").click()
    driver.find_element_by_id(("username")).send_keys("tomsmith")
    driver.find_element_by_id(("password")).click()
    driver.find_element_by_id(("password")).send_keys("SuperSecretPassword!")
    driver.find_element_by_xpath('//*[@id="login"]/button/i').click()
    wait = WebDriverWait(driver, 500)
    url = driver.current_url
    assert (url == "http://the-internet.herokuapp.com/secure")
    driver.quit()