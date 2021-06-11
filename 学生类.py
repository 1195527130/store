class Student:
    __name = ""
    __age = 0

    def setName(self,name):
        self.__name = name

    def setAge(self,age):
        if age < 0 or age > 120:
            print("输入非法")
        else:
            self.__age = age

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getInfo(self):
        print("大家好，我叫",self.__name,",今年",self.__age,"岁了!")

    def equalAge(self,student):
        if student.getAge() == self.__age :
            return "我和" + student.getName() + "一样大!"
        elif student.getAge() > self.__age :
            return student.getName() + "比我大" + str(student.getAge() - self.__age) + "岁!"
        else :
            return student.getName() + "比我小" + str(self.__age - student.getAge()) + "岁!"

class testST:
    me = Student()
    me.setName("张三")
    me.setAge(18)
    classmate = Student()
    classmate.setName("李四")
    classmate.setAge(20)
    me.getInfo()
    print(me.equalAge(classmate))




















