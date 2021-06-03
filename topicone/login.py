from selenium import webdriver

class Login_page :
    def __init__(self,driver):
        self.driver = driver

    def login(self,username,password):
        self.driver.find_element_by_id("").send_keys(username)
        self.driver.find_element_by_id("").send_keys(password)
        self.driver.find_element_by_id("").click()

    def get_success_login(self):
        return self.driver.title

    def get_error_password_login(self):
        return self.driver.find_element_by_id('').text

class return_page :
    def __init__(self,driver):
        self.driver = driver

    def return_bill(self,username,password,lianxiren,phone,money,date,zhaiyao,money1,beizhu,bufu):
        '''
            id 中填入对应按键的id值
            frame 中填入对应的模块名
        '''
        self.driver.find_element_by_id("").send_keys(username)
        self.driver.find_element_by_id("").send_keys(password)
        self.driver.find_element_by_id("").click()                      # 登录系统
        self.driver.find_element_by_id("").click()                      # 进入对账单回签界面
        self.driver.find_element_by_id("").send_keys("余额对账单回签")     # 下拉列表中填入余额对账单回签
        self.driver.find_element_by_id("").click()                      # 点击确定
        self.driver.find_element_by_id("").click()                      # 选择账期
        self.driver.find_element_by_id("").click()                      # 勾选核对正确结果，多条记录就勾选多次
        self.driver.find_element_by_id("").click()                      # 点击对账不符情况表
        self.driver.find_element_by_id("").send_keys(lianxiren)         # 输入单位联系人名称
        self.driver.find_element_by_id("").send_keys(phone)             # 输入联系电话
        self.driver.find_element_by_id("").send_keys(money)             # 输入单位余额
        self.driver.find_element_by_id("").click()                      # 点击添加
        self.driver.find_element_by_id("").send_keys(date)              # 输入日期
        self.driver.find_element_by_id("").send_keys(zhaiyao)           # 输入摘要
        self.driver.find_element_by_id("").send_keys(money1)            # 输入金额
        self.driver.find_element_by_id("").send_keys(beizhu)            # 输入备注
        self.driver.find_element_by_id("").click()                      # 点击确定
        self.driver.find_element_by_id("").click()                      # 点击反馈信息表
        self.driver.find_element_by_id("").click()                      # 勾选no选项
        self.driver.find_element_by_id("").send_keys(bufu)              # 输入不服说明
        self.driver.find_element_by_id("").click()                      # 点击提交
        self.driver.find_element_by_id("").click()                      # 点击回签

    def return_bill_success(self):
        return self.driver.title








































