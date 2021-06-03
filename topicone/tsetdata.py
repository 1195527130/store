class login_data :
    login_success = {
        "username" : "a123456",
        "password" : "a1234567",
        "expect" : "中信银行公司网上银行"
    }

    login_fail_username = {
        "username" : "a123",
        "password" : "a1234567",
        "expect" : "登录失败！"
    }

    login_fail_password = {
        "username": "b1234567",
        "password": "a1234",
        "expect": "登录失败！"
    }

    login_fail_all = {
        "username": "c1234",
        "password": "c1234",
        "expect": "登录失败！"
    }