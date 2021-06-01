'''
有旅游城市显示
进入列表后显示旅游城市下级地名

到最终城市后，显示商品列表
可以通过输入商品编号进行购物
'''
system = {
    "海南" : {
        "海口" : {
            "椰子" : 15,
            "香蕉" : 6,
            "榴莲" : 8
        },
        "三亚" : {
            "贝壳" : 10,
            "鹅卵石" : 8,
            "细沙" : 3
        }
    },
    "北京" : {
        "朝阳区" : {
            "老北京拖鞋" : 10,
            "四合院拼图" : 40
        },
        "海淀区" : {
            "老北京剪纸" : 20,
            "泥人彩塑" : 15,
            "明信片" : 30
        }
    },
    "河南" : {
        "开封" : {
            "开封汴绣" : 30,
            "木板年画" : 20
        },
        "郑州" : {
            "唐三彩" : 100,
            "独山玉" : 120,
            "澄泥砚" : 50
        }
    }
}
print("欢迎使用旅游系统！")
mycar = []
cost = 0
while True :
    print("--------------------")
    print("您可以选择前往以下地区：")
    for key in system :
        print(key,"\t",end='')
    print()
    go1 = input("请输入您想去的地方：")
    if go1 in system :
        while True :
            print("------------------------")
            print("您已经到",go1,"了，接下来想去哪呢？")
            for key1 in system[go1] :
                print(key1, "\t", end='')
            print()
            go2 = input("请输入您想去的地方：")
            if go2 in system[go1] :
                while True:
                    print("------------------------")
                    print("您已经到", go2, "了，要不要买点纪念品呢？")
                    for key2 in system[go1][go2]:
                        print(key2, "\t", end='')
                    print()
                    money = input("先看看您带了多少钱把：")
                    if money.isdigit() :
                        money = int(money)
                        while True :
                            print("---------------------------")
                            for key2 in system[go1][go2]:
                                print(key2, "\t", end='')
                            print()
                            shop = input("请输入您想购买的东西：")
                            if shop in system[go1][go2]:
                                if money >= system[go1][go2].get(shop) :
                                    mycar.append([shop,system[go1][go2].get(shop)])
                                    money = money - system[go1][go2].get(shop)
                                    print("购买成功！您还有",money,"元！")
                                else :
                                    print("您带的钱不够噢！")
                            elif shop == 'q' or shop == 'Q':
                                break
                            else:
                                print("没有您说的商品噢！")
                    elif money == 'q' or money == 'Q' :
                        break
                    else :
                        print("输入的金额不对噢！")
            elif go2 == 'q' or go2 == 'Q':
                break
            else:
                print("还不支持去您说的地方噢！")
    elif go1 == 'q' or go1 == 'Q' :
        print("等待您下次使用！")
        break
    else :
        print("还不支持去您说的地方噢！")
print("-------------------------------")
print("您本次旅游购买的商品有：")
for index,value in enumerate(mycar) :
    cost = cost + value[1]
    print(value[0])
print("总共花费了：",cost,"元！")