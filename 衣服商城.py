id1 = 1
name1 = "牛仔裤"
price1 = 88
num1 = 30
produce1 = "优衣库"

id2 = 2
name2 = "衬衫"
price2 = 66
num2 = 30
produce2 = "优衣库"

id3 = 3
name3 = "T恤"
price3 = 68
num3 = 50
produce3 = "古驰"

id4 = 4
name4 = "羽绒服"
price4 = 89
num4 = 50
produce4 = "海澜之家"


print("==============欢迎来到符懿衣服商城=================")
print("-----------------------------------------------")
print("编号       名称      价格      数量      品牌      ")
print(id1,"       ",name1,"   ",price1,"     ",num1,"    ",produce1)
print(id2,"       ",name2,"     ",price2,"     ",num2,"    ",produce2)
print(id3,"       ",name3,"      ",price3,"     ",num3,"    ",produce3)
print(id4,"       ",name4,"   ",price4,"     ",num4,"    ",produce4)
print("-----------------------------------------------")
print("总价格：",(price1 * num1 + price2 * num2 + price3 * num3 + price4 * num4),"元")