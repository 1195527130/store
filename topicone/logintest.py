from selenium import webdriver
from ddt import ddt         # 数据驱动测试
from ddt import data        # 获取数据包
from ddt import unpack      # 将数据解包
import unittest
from testdata import login_data
from testdata import return_bill_data
from login import Login_page
from login import return_page
import time

@ddt        # 编写驱动程序
class LoginTest(unittest.TestCase):

    def setUp(self) -> None:        # 驱动开始时
        self.driver = webdriver.Chrome()
        self.driver.get("项目网站")
        self.driver.maximize_window()

    def tearDown(self) -> None:     # 驱动结束时
        time.sleep(2)
        self.driver.quit()

    @data(*login_data.login_success)
    def test_success_login(self,testdata):
        login = Login_page(self.driver)      # 创建页面操作逻辑对象

        login.login(testdata["username"],testdata["password"])
        time.sleep(3)
        result = login.get_success_login()  # 通过之前设定的方法获取实际结果

        expect = testdata["expect"]

        self.assertEqual(expect,result)     # 通过断言判断用例执行是否通过

    @data(*login_data.login_fail_username)
    def test_error_password_login(self, testdata):
        login = Login_page(self.driver)
        login.login(testdata["username"], testdata["password"])
        time.sleep(3)
        result = login.get_error_password_login()
        expect = testdata["expect"]
        self.assertEqual(expect, result)

    @data(*login_data.login_fail_password)
    def test_error_password_login(self, testdata):
        login = Login_page(self.driver)
        login.login(testdata["username"], testdata["password"])
        time.sleep(3)
        result = login.get_error_password_login()
        expect = testdata["expect"]
        self.assertEqual(expect, result)

    @data(*login_data.login_fail_all)
    def test_error_password_login(self, testdata):
        login = Login_page(self.driver)
        login.login(testdata["username"], testdata["password"])
        time.sleep(3)
        result = login.get_error_password_login()
        expect = testdata["expect"]
        self.assertEqual(expect, result)

    @data(*return_bill_data.return_bill_success)
    def test_success_return_bill(self,testdata):
        rebill = return_page(self.driver)
        rebill.return_bill(testdata["username"], testdata["password"], testdata["lianxiren"], testdata["phone"],
                           testdata["money"], testdata["date"], testdata["zhaiyao"], testdata["money1"],
                           testdata["beizhu"], testdata["bufu"], )
        time.sleep(3)
        expect = testdata["expect"]
        result = rebill.return_bill_success()
        self.assertEqual(expect,result)



















