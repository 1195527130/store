from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("F:/python自动化测试/自动化测试/练习的html/跳转页面/pop.html")
driver.find_element_by_xpath("//*[@id='goo']").click()
time.sleep(10)
driver.quit()