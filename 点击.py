from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get(r"F:/python自动化测试/自动化测试/练习的html/弹框的验证/dialogs.html")

driver.find_element_by_xpath("//*[@id='alert']").click()
time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(2)

driver.find_element_by_xpath("//*[@id='confirm']").click()
time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(2)

driver.find_element_by_xpath("//*[@id='confirm']").click()
time.sleep(3)
driver.switch_to.alert.dismiss()
time.sleep(2)

driver.quit()