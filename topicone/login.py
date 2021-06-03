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

