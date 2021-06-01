import random
'''
6张联想8折卷

4张苹果7折卷


'''
shop = [
    ["海尔空调",30000],
    ["联想电脑",5000],
    ["联想手机",2000],
    ["苹果笔记本电脑",18000],
    ["苹果手机",12000],
    ["卫龙辣条",1],
    ["可乐",3]
]
print("------欢迎来到汤姆的商城-------")
print("-------今天有如下商品：--------")
for index,value in enumerate(shop) :
    print(index,"",value)
salary = int(input("请输入您的钱包余额："))
flag = random.randint(1,100)
if flag >= 1 and flag <= 6 :
    print("恭喜您获得了一张联想八折卷，只可以在本次购物中使用！")
elif flag > 6 and flag <= 10 :
    print("恭喜您获得了一张苹果七折卷，只可以在本次购物中使用！")
else :
    print("很可惜，本次没有购物卷！")
mycar = []
while True :
    print("现在有以下商品：")
    for index,value in enumerate(shop) :
        print(index,"",value)
    num = input("请输入想要的商品编号：")
    if num.isdigit() :
        num = int(num)
        if num > len(shop) :
            print("输入的商品编号不存在，请重新输入！")
        elif (num == 1 or num == 2) and (flag >= 1 and flag <= 6) :
            if salary >= shop[num][1] * 0.8 :
                mycar.append([shop[num][0],shop[num][1] * 0.8])
                salary = salary - shop[num][1] * 0.8
                flag = 101
                print("购买成功，您的余额还有：",salary,"元!")
            else :
                print("您的余额不足，购买失败！")
        elif (num == 3 or num == 4) and (flag > 6 and flag <= 10) :
            if salary >= shop[num][1] * 0.7 :
                mycar.append([shop[num][0],shop[num][1] * 0.7])
                salary = salary - shop[num][1] * 0.7
                flag = 101
                print("购买成功，您的余额还有：",salary,"元!")
            else :
                print("您的余额不足，购买失败！")
        else :
            if salary >= shop[num][1] :
                mycar.append(shop[num])
                salary = salary - shop[num][1]
                print("购买成功，您的余额还有：", salary, "元!")
            else:
                print("您的余额不足，购买失败！")
    elif num == 'q' or num == 'Q' :
        print("欢迎下次光临！")
        break
    else :
        print("输入非法！请重新输入！")

money = 0
print("购物结束，本次购买的商品如下：")
for index,value in enumerate(mycar) :
    money = money + value[1]
    print(value)
print("本次总共消费了",money,"元！")