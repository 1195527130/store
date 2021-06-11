class People :
    __name = ""
    __age = 0
    __sex = ""
    __phonemoney = 0
    __phonename = ""
    __phoneele = 0
    __phonesize = ""
    __phonedate = 0
    __integral = 0

    def __init__(self,name,age,sex,phonemoney,phonename,phoneele,phonesize,phonedate,integral):
        self.__name = name
        self.__age = age
        self.__sex = sex
        self.__phonemoney = phonemoney
        self.__phonename = phonename
        self.__phoneele = phoneele
        self.__phonesize = phonesize
        self.__phonedate = phonedate
        self.__integral = integral

    def sell(self,message):
        print("发出了：",message)

    def getInfo(self):
        print("还有",self.__phonemoney,"元话费，",self.__integral,"分积分！")

    def call(self,phonenum,time):
        if len(phonenum) != 0 :
            if self.__phonemoney >= 1 :
                print("波通电话。。。")
                if time in range(0,11):
                    self.__phonemoney = self.__phonemoney - time * 1
                    self.__integral = self.__integral + time * 15
                    return time * 1
                elif time in range(11,21):
                    self.__phonemoney = self.__phonemoney - time * 0.8
                    self.__integral = self.__integral + time * 39
                    return time * 0.8
                else:
                    self.__phonemoney = self.__phonemoney - time * 0.65
                    self.__integral = self.__integral + time * 48
                    return time * 0.65
            else :
                print("您的话费余额不足")
        else:
            print("请输入对方电话！")

# a = People("张三",18,"男",20,"华为",60,"720x480",20,0)
# a.sell("欢迎光临！")
# money = a.call("123",30)
# print("扣费了",money,"元！")




