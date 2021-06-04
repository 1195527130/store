import random

names = {}


welcome = '''
    --------------------------------------
    ---     中国工商银行账户管理系统     -----
    --------------------------------------
    - 1、开户                             -
    - 2、存钱                             -
    - 3、取钱                             -
    - 4、转账                             -
    - 5、查询                             -
    - 6、再见                             -
    --------------------------------------
'''

info = '''
    ----------个人信息 【工商银行】--------
    用户名：%s,
    密码：%s,
    账号：%s,
    余额：%s,
    国家：%s,
    省份：%s,
    街道:%s,
    门牌号：%s
    开户行名称：%s
    ------------------------------------
'''
bank_name = '中国工商银行昌平支行'

def getRandom() :
    id = ''
    for i in range(0,8) :
        id = id + random.sample("ABCDEFGHIJKLNMOPQRSTUVWXYZabcdefghijklnmopqrstuvwxyz1234567890", 1)[0]
    return id

def bank_addUser(account,username,password,money,country,province,street,door):
    if len(names)  >= 100:
        return 3
    # 2.判断是否存在:依据是用户名
    if account in names:
        return 2
    names[account] = {
        "username":username,
        "password":password,
        "account":account,
        "money":money,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "bank_name":bank_name
    }
    return 1

def bank_saveMoney(account,money) :      # 赵丽雪
    if account in names:
        names[account]["money"] = names[account].get("money") + money
        return True
    else:
        return False

def bank_takeMoney(account, password, money) :
    if account not in names :
        return 1
    if names[account].get("password") != password:
        return 2
    if names[account].get("money") < money :
        return 3
    names[account]["money"] = names[account].get("money") - money
    return 0

def bank_changeMoney(outid, inid, password, money):
    if outid not in names or inid not in names :
        return 1
    if names[outid].get("password") != password :
        return 2
    if names[outid].get("money") < money :
        return 3
    names[outid]["money"] = names[outid].get("money") - money
    names[inid]["money"] = names[inid].get("money") + money
    return 0

def bank_getInfo(account,password):         # 刘佳明
    if account not in names:
        return 1
    if password != names[account]["password"]:
        return 2
    print(info % (names[account].get("username"), names[account].get("password"), names[account].get("account"),
                  names[account].get("money"), names[account].get("country"), names[account].get("province"),
                  names[account].get("street"), names[account].get("door"), bank_name))
    return 3

def addUser():
    print("----------开户界面----------")
    username = input("请输入您的姓名：")
    password = input("请输入你的密码：")
    money = int(input("请输入您的账户余额：")) # "123"  123
    print("下面请输入您的个人地址信息：")
    country = input("请输入您的国籍：")
    province =  input("请输入您的省份：")
    street = input("请输入您的居住街道：")
    door = input("请输入您的门牌号：")
    account = getRandom()
    status = bank_addUser(account,username,password,money,country,province,street,door)
    if status == 1:
        print("恭喜开户成功！以下是您的个人信息：")
        print(info % (username,password,account,money,country,province,street,door,bank_name))
    elif status == 2:
        print("对不起，您的账户已存在！请勿重复开户！")
    elif status == 3:
        print("对不起，用户库已满，请携带证件到其他银行办理！")

def saveMoney() :       # 赵丽雪
    account = input("请输入您的账户：")
    getmoney = int(input("请输入您要存入的金额："))
    bools = bank_saveMoney(account, getmoney)
    if bools == True:
        print("恭喜您，存钱成功！您的余额为：", names[account].get("money"))
    if bools == False:
        print("用户不存在！")

def takeMoney() :
    print("----------取款界面----------")
    account = input("请输入账号：")
    password = input("请输入密码：")
    money = int(input("请输入取款金额："))
    a = bank_takeMoney(account, password, money)
    if a == 0:
        print("取款成功，当前余额为：", names[account].get("money"), "元")
    elif a == 1:
        print("该账户不存在，请重试！")
    elif a == 2:
        print("密码错误，请重试！")
    elif a == 3:
        print("账户余额不足！")

def changeMoney() :
    print("----------转账界面----------")
    outid = input("请输入付款账户：")
    inid = input("请输入收款账户：")
    password = int(input("请输入密码："))
    money = int(input("请输入转账金额："))
    a = bank_changeMoney(outid, inid, password, money)
    if a == 0:
        print("转账成功！")
    elif a == 1:
        print("付款账户或收款账户不存在，请重试！")
    elif a == 2:
        print("密码错误，请重试！")
    elif a == 3:
        print("付款账户余额不足！")

def getInfo() :         # 刘佳明
    account = input("请输入您要查询的账号：")
    password = input("请输入您要查询的账户密码：")
    status1 = bank_getInfo(account, password)
    if status1 == 1:
        print("账号错误")
    elif status1 == 2:
        print("密码错误")
    elif status1 == 3:
        print("查询成功")


while True :
    print(welcome)
    a = input("请输入业务编号：")
    if a == '1' :
        addUser()
    elif a == '2' :
        saveMoney()
    elif a == '3' :
        takeMoney()
    elif a == '4' :
        changeMoney()
    elif a == '5':      # 刘佳明
        getInfo()
    elif a == '6':
        print("等待您的下次使用!")
        break
    else :
        print("输入非法！")




















