class Student:
    __num = 0
    __name = ""
    __age = 0
    __sex = ""
    __high = 0
    __weight = 0
    __score = 0
    __addr = ""
    __phone = ""

    def __init__(self,num,name,age,sex,high,weight,score,addr,phone):
        self.__num = num
        self.__name = name
        self.__age = age
        self.__sex = sex
        self.__high = high
        self.__weight = weight
        self.__score = score
        self.__addr = addr
        self.__phone = phone

    def study(self,time):
        print(self.__name,"学习了",time,"分钟！")

    def play(self,game):
        print(self.__name, "正在玩", game)

    def program(self,row):
        print(self.__name,"编写了",row,"行代码！")

    def sum(self,*args):
        num = 0
        for arg in args :
            num = num + arg
        return num

class car:
    __name = ""
    __wheel = 0
    __color = ""
    __weight = ""
    __oil = 0

    def __init__(self,name,wheel,color,weight,oil):
        self.__name = name
        self.__wheel = wheel
        self.__color = color
        self.__weight = weight
        self.__oil = oil

    def run(self,type):
        print(self.__name,"正在",type)

class laptop:
    __name = ""
    __keeptime = 0
    __color = ""
    __weight = ""
    __cpu = ""
    __RAMsize = ""
    __disksize = ""

    def playgame(self,game):
        print("打开了",game)

    def work(self):
        print("正在办公！")

class monkey:
    __type = ""
    __sex = ""
    __color = ""
    __weight = ""

    def createfire(self,stuff):
        print("正在使用",stuff,"造火！")

    def study(self,*args):
        for arg in args :
            print("正在学习",arg)
















