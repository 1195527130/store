from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.get("http://8.129.91.152:8765/Index/reg.html")
driver.maximize_window()

driver.find_element_by_xpath("//*[@id='phone']").send_keys("18339195555")

time.sleep(10)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[3]/a").click()
# txt = driver.find_element_by_class_name("layui-layer-content").text
# time.sleep(1)

time.sleep(10)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[4]/input").send_keys("a1234567")
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[5]/label/input").click()
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[6]/button").click()
# print(txt)
time.sleep(5)

driver.quit()





























