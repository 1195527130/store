class Air_conditioning :
    __price = 0
    __name = ""

    def setPrice(self,price):
        self.__price = price

    def setName(self,name):
        self.__name = name

    def getPrice(self):
        return self.__price

    def getName(self):
        return self.__name

    def start(self):
        print("空调开机了。。。")

    def stop(self,time):
        print("空调将在",time,"分钟后自动关闭。。。")

class testAC:
    ac = Air_conditioning()
    ac.setName("海尔")
    ac.setPrice(600.0)
    print(ac.getName())
    print(ac.getPrice())
    ac.start()
    ac.stop(10)







