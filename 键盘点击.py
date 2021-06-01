from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
ele = driver.find_element_by_xpath("//*[@id='kw']")
ac = ActionChains(driver)
ac.send_keys_to_element(ele,"java").key_down(Keys.ENTER).perform()
time.sleep(5)
driver.quit()