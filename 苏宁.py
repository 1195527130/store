from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://www.suning.com/")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='searchKeywords']").send_keys("iphone 12")
driver.find_element_by_xpath("//*[@id='searchSubmit']").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='0000000000-12122946310']/div").click()

wins = driver.window_handles
driver.switch_to.window(wins[1])
ac = ActionChains(driver)
driver.find_element_by_xpath("//*[@id='colorItemList']/dd/ul/li[11]/a").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='versionItemList']/dd/ul/li[3]/a").click()
time.sleep(2)
ele3 = driver.find_element_by_xpath("//*[@id='addCart']")
ac.click(ele3).perform()
time.sleep(5)
driver.quit()