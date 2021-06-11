class People:
    __name = ""
    __sex = ""
    __age = 0
    def __init__(self,name,sex,age):
        self.__name = name
        self.__sex = sex
        self.__age = age

    def setName(self, name):
        self.__name = name

    def setSex(self,sex):
        self.__sex = sex

    def setAge(self, age):
        self.__age = age

    def getName(self):
        return self.__name

    def getSex(self):
        return self.__sex

    def getAge(self):
        return self.__age

class Worker(People):
    def work(self):
        print(super().getName(),"正在干活!")

class Student(People):
    __number = ""
    def __init__(self,name,sex,age,number):
        People.__init__(self,name,sex,age)
        self.__number = number

    def setNumber(self,number):
        self.__number = number

    def getNumber(self):
        return self.__number

    def sing(self):
        print(self.getName(),"正在唱歌...")

    def study(self):
        print(self.getName(),"正在学习...")

class Test:
    stu = Student("张楚岚","男",18,"001")
    print(stu.getName())
    print(stu.getSex())
    print(stu.getAge())
    print(stu.getNumber())
    stu.sing()
    stu.study()





















