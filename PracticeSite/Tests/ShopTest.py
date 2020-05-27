from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains

with Chrome() as driver:
    driver.maximize_window()
    driver.get("http://automationpractice.com/index.php")
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


