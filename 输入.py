from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get(r"F:/python自动化测试/自动化测试/练习的html/上传文件和下拉列表/autotest.html")

driver.find_element_by_xpath("//*[@id='accountID']").send_keys("python")
driver.find_element_by_xpath("//*[@id='passwordID']").send_keys("123456")
driver.find_element_by_xpath("//*[@id='areaID']").send_keys("北京市")
driver.find_element_by_xpath("//*[@id='sexID2']").click()
driver.find_element_by_xpath("//*[@value='spring']").click()
driver.find_element_by_xpath("//*[@value='winter']").click()
driver.find_element_by_xpath("//*[@name='file']").send_keys("F:\python自动化测试\专题项目\业务整理表.xlsx")
driver.find_element_by_xpath("//*[@id='buttonID']").click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='accountID']").clear()
time.sleep(2)
driver.quit()
