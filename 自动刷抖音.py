from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

server = r'http://localhost:4723/wd/hub'

desired_capabilities = {
  "platformName": "Android",
  "platformVersion": "7.1.2",
  "deviceName": "127.0.0.1:62001",
  "appPackage": "com.ss.android.ugc.aweme",
  "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity"
}
driver = webdriver.Remote(server, desired_capabilities)

'''
driver.find_element_by_id("com.android.settings:id/title").click()  # 点击wlan
#time.sleep(2)
driver.find_element_by_class_name("android.widget.ImageButton").click()  # 点击返回
#time.sleep(2)
driver.find_element_by_xpath("//*[contains(@text, '更多')]").click()  # 点击更多
#time.sleep(2)
driver.find_element_by_xpath("//*[contains(@content-desc, '向上')]").click()  # 点击返回
#time.sleep(2)
driver.quit()
'''

time.sleep(10)
for i in range(1,5) :
  TouchAction(driver).press(x=540, y=1459).move_to(x=561, y=499).release().perform()
  TouchAction(driver).wait(10000)

driver.quit()









