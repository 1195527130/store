from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("F:/python自动化测试/自动化测试/练习的html/main.html")
driver.switch_to.frame("frame")
driver.find_element_by_xpath("//*[@id='input1']").send_keys("java")
time.sleep(2)
driver.quit()