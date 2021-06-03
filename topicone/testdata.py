class login_data :
    login_success = {
        "username" : "a123456",
        "password" : "991001",
        "expect" : "中信银行公司网上银行"
    }

    login_fail_username = {
        "username" : "a123",
        "password" : "a1234567",
        "expect" : "登录失败！"
    }

    login_fail_password = {
        "username": "b1234567",
        "password": "991081",
        "expect": "登录失败！"
    }

    login_fail_all = {
        "username": "c1234",
        "password": "963214",
        "expect": "登录失败！"
    }

class return_bill_data :
    return_bill_success = {
        "username": "a123456",
        "password": "991001",
        "lianxiren":"张三",
        "phone":"13333333333",
        "money":"500000.0",
        "date":"2021.06.01",
        "zhaiyao":" ",
        "money1":"2000.0",
        "beizhu":"转账",
        "bufu":"没有此项交易",
        "expect":"中信银行公司网上银行"
    }