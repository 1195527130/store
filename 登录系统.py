count = 0
while True :
    name = input("请输入用户名：")
    password = input("请输入密码：")
    count = count + 1
    if count < 3 :
        if name == "root" and password == "admin" :
            print("登录成功！")
            break
        else :
            print("登录失败！请重新输入用户名和密码！")
    else :
        print("失败次数达到三次，无法登录")
        break