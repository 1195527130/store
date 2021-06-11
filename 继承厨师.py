class Cook:
    __name = ""
    __age = 0

    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def setName(self,name):
        self.__name = name

    def setAge(self,age):
        self.__age = age

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def cook_rice(self):
        print("煮饭")


class CookSon(Cook):
    def cook_vegetable(self):
        print("炒菜")

class CookGrandson(CookSon):
    def cook_rice(self):
        print("正在煮饭....")

    def cook_vegetable(self):
        print("正在炒菜....")

class test:
    cook = CookGrandson("王也",18)
    print("厨师的名字为:",cook.getName(),"，厨师的年龄为:",cook.getAge())
    cook.cook_rice()
    cook.cook_vegetable()


























