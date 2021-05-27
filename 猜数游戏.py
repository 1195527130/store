import random
num = random.randint(1,100)
money = 5000
count = 0
while True :
    money = money - 500
    count = count + 1
    if count = 7 :
        print("次数用尽~")
        break
    if money >= 0 :
        a = int(input("请输入数字："))
        if a == num :
            if count <= 3 :
                print("恭喜你！猜对了！获得两百元奖励~")
                break
            else :
                print("猜对了！恭喜你！你猜了",count,"次")
                break
        elif a > num :
            print("猜大了噢！")
        else :
            print("猜小了噢！")
    else :
        print("您没钱了噢~")
        break

print("答案为：",num)