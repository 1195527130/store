from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

server = r'http://localhost:4723/wd/hub'

desired_capabilities = {
  "platformName": "Android",
  "platformVersion": "7.1.2",
  "deviceName": "127.0.0.1:62001",
  "appPackage": "com.zhihu.android",
  "appActivity": "com.zhihu.android.app.ui.activity.MainActivity"
}
driver = webdriver.Remote(server, desired_capabilities)


time.sleep(10)
TouchAction(driver).tap(x=532, y=944).perform()
el1 = driver.find_element_by_id("com.zhihu.android:id/login_username")
el1.send_keys("1195527130@qq.com")
el2 = driver.find_element_by_id("com.zhihu.android:id/login_password")
el2.send_keys("a1195527130")
time.sleep(10)
TouchAction(driver).tap(x=507, y=816).perform()
time.sleep(10)
TouchAction(driver).tap(x=614, y=103).perform()
time.sleep(3)
el5 = driver.find_element_by_id("com.zhihu.android:id/input")
el5.send_keys("ipone")
# TouchAction(driver).tap(x=940, y=375).perform()
# TouchAction(driver).tap(x=78, y=445).perform()
time.sleep(3)
TouchAction(driver).tap(x=808, y=198).perform()
time.sleep(3)
TouchAction(driver).tap(x=148, y=338).perform()
time.sleep(3)
TouchAction(driver).tap(x=594, y=1715).perform()
time.sleep(3)
driver.quit()