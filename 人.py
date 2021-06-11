class People:
    def __init__(self,name,age,sex,job):
        self.name = name
        self.age = age
        self.sex = sex
        self.job = job

    def work(self):
        print(self.name,"去做",self.job,"了。")

    def run(self,min):
        print(self.name,"跑步了",min,"分钟")

    def smoke(self,smoke):
        print(self.name,"正在抽",smoke)

    def eat(self,foot):
        print(self.name,"正在吃",foot)

    def drink(self,drink):
        print(self.name,"正在喝",drink)

a = People("邢龙",16,"男","小白脸")
a.work()
a.run(10)
a.smoke("红双喜")
a.eat("炒饼")
a.drink("冰雪碧")

















