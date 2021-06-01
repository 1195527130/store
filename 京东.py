from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://www.jd.com/")
driver.maximize_window()
driver.find_element_by_link_text("你好，请登录").click()
driver.find_element_by_xpath("//*[@id='content']/div[2]/div[1]/div/div[3]").click()
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("18339195985")
driver.find_element_by_xpath("//*[@id='nloginpwd']").send_keys("a1195527130")
driver.find_element_by_xpath("//*[@id='loginsubmit']").click()
time.sleep(2)
# driver.find_element_by_xpath("//*[@id='app']/div/div/div/div[2]/button").click()
# driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div/div/div[1]/button").click()
# time.sleep(15)
# driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div/div[3]/button").click()
# time.sleep(5)
driver.find_element_by_xpath("//*[@id='key']").send_keys("iphone 12")
driver.find_element_by_xpath("//*[@id='search']/div/div[2]/button").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='J_goodsList']/ul/li[3]/div/div[1]/a/img").click()
wins = driver.window_handles
driver.switch_to.window(wins[1])
driver.find_element_by_xpath("//*[@id='choose-attr-1']/div[2]/div[3]").click()
driver.find_element_by_xpath("//*[@id='choose-attr-2']/div[2]/div[1]/a").click()
driver.find_element_by_xpath("//*[@id='InitCartUrl']").click()
time.sleep(5)
driver.quit()

