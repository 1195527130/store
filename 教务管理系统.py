import random
list1= ["张三","李四","王五","路人甲","炮灰乙"]
print("----------欢迎使用教务管理系统-----------")
print("-------------------------------------")
print("1.随机点名")
print("2.随机处罚")
print("3.退出")
while True :
    a = int(input("请输入业务编号："))
    if a == 1 :
        index = random.randint(0,len(list1)-1)
        print("恭喜",list1[index],"同学！您被抽中了！")
    if a == 2 :
        if len(list1) > 0 :
            index = random.randint(0, len(list1)-1)
            chose = random.randint(0,201)
            print("恭喜",list1[index],"同学！您被罚抄",chose,"遍！")
            list1.remove(list1[index])
        else :
            print("已经没有学生了！")
    if a == 3 :
        print("下次再见！")
        break