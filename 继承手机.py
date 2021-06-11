class OldPhone:
    __phonename = ""

    def __init__(self,phonename):
        self.__phonename = phonename

    def setName(self,phonename):
        self.__phonename = phonename

    def getName(self):
        return self.__phonename

    def call(self,name):
        print("正在给",name,"打电话...")

class NewPhone(OldPhone):
    def call(self,name):
        print("语音拨号中...")
        super().call(name)

    def show(self):
        print("品牌为：",super().getName(),"的手机真好用!")


class test:

    phone = NewPhone("摩托罗拉")
    phone.setName("华为")
    phone.show()
    phone.call("冯宝宝")



































