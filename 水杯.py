class glass:
    __high = 0
    __capacity = 0
    __color = ""
    __stuff = ""

    def __init__(self,high,capacity,color,stuff):
        self.__high = high
        self.__capacity = capacity
        self.__color = color
        self.__stuff = stuff

    def savewater(self,num,watertype):
        if num <= self.__capacity :
            print("存放了",num,"毫升的",watertype)
        else:
            print("存放不了",num,"毫升的",watertype)










