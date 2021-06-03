from selenium import webdriver
from ddt import ddt         # 数据驱动测试
from ddt import data        # 获取数据包
from ddt import unpack      # 将数据解包
import unittest
from tsetdata import login_data
from login import Login_page
import time

@ddt        # 编写驱动程序
class LoginTest(unittest.TestCase):

    def setUp(self) -> None:        # 驱动开始时
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.jasonisoft.cn:8080/HKR")
        self.driver.maximize_window()

    def tearDown(self) -> None:     # 驱动结束时
        time.sleep(2)
        self.driver.quit()

    @data(*login_data.succerss_data)
    def test_success_login(self,testdata):
        login = Login_page(self.driver)      # 创建页面操作逻辑对象

        login.login(testdata["username"],testdata["password"])
        time.sleep(3)
        result = login.get_success_login()  # 通过之前设定的方法获取实际结果

        expect = testdata["expect"]

        self.assertEqual(expect,result)     # 通过断言判断用例执行是否通过

    @data(*login_data.password_error_data)
    def test_error_password_login(self, testdata):
        login = Login_page(self.driver)
        login.login(testdata["username"], testdata["password"])
        time.sleep(3)
        result = login.get_error_password_login()
        expect = testdata["expect"]
        self.assertEqual(expect, result)