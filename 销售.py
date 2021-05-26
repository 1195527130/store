date1 = 1
name1 = "羽绒服"
price1 = 253.6
num1 = 500
sell1 = 10

date2 = 2
name2 = "牛仔裤"
price = 286.3
num2 = 600
sell2 = 60

date3 = 3
name3 = "风衣"
price3 = 96.8
num3 = 335
sell3 = 43

date4 = 4
name4 = "皮草"
price4 = 135.9
num4 = 855
sell4 = 63

date5 = 5
name5 = "T恤"
price5 = 65.8
num5 = 632
sell5 = 63

date6 = 6
name6 = "衬衫"
price6 = 49.3
num6 = 562
sell6 = 120

date7 = 7
name7 = "牛仔裤"
price7 = 86.3
num7 = 600
sell7 = 72

date8 = 8
name8 = "羽绒服"
price8 = 253.6
num8 = 500
sell8 = 69

date9 = 9
name9 = "牛仔裤"
price9 = 86.3
num9 = 600
sell9 = 35

date10 = 10
name10 = "羽绒服"
price10 = 253.6
num10 = 500
sell10 = 140

date11 = 11
name11 = "牛仔裤"
price11 = 86.3
num11 = 600
sell11 = 90

date12 = 12
name12 = "皮草"
price12 = 135.9
num12 = 855
sell12 = 24

date13 = 13
name13 = "T恤"
price13 = 65.8
num13 = 632
sell13 = 45

date14 = 14
name14 = "风衣"
price14 = 96.8
num14 = 335
sell14 = 25

date15 = 15
name15 = "牛仔裤"
price15 = 86.3
num15 = 600
sell15 = 60

date16 = 16
name16 = "T恤"
price16 = 65.8
num16 = 632
sell16 = 129

date17 = 17
name17 = "羽绒服"
price17 = 253.6
num17 = 500
sell17 = 10

date18 = 18
name18 = "风衣"
price18 = 96.8
num18 = 335
sell18 = 43

date19 = 19
name19 = "T恤"
price19 = 65.8
num19 = 632
sell19 = 63

date20 = 20
name20 = "牛仔裤"
price20 = 86.3
num20 = 600
sell20 = 60

date21 = 21
name21 = "皮草"
price21 = 135.9
num21 = 855
sell21 = 63

date22 = 22
name22 = "风衣"
price22 = 96.8
num22 = 335
sell22 = 60

date23 = 23
name23 = "T恤"
price23 = 65.8
num23 = 632
sell23 = 58

date24 = 24
name24 = "牛仔裤"
price24 = 86.3
num24 = 600
sell24 = 140

date25 = 25
name25 = "T恤"
price25 = 65.8
num25 = 632
sell25 = 48

date26 = 26
name26 = "风衣"
price26 = 96.8
num26 = 335
sell26 = 43

date27 = 27
name27 = "皮草"
price27 = 135.9
num27 = 855
sell27 = 57

date28 = 28
name28 = "羽绒服"
price28 = 253.6
num28 = 500
sell28 = 10

date29 = 29
name29 = "T恤"
price29 = 65.8
num29 = 632
sell29 = 63

date30 = 30
name30 = "风衣"
price30 = 96.8
num30 = 335
sell30 = 78

zsell = sell1 + sell2 + sell3 + sell4 + sell5 + sell6 + sell7 + sell8 + sell9 + sell10 + sell11 + sell12 + sell13 + sell14 + sell15 + sell16 + sell17 + sell18 + sell19 + sell20 + sell21 + sell22 + sell23 + sell24 + sell25 + sell26 + sell27 + sell28 + sell29 + sell30

yprice = (sell1 + sell8 + sell10 + sell17 + sell28) * 253.6
nprice = (sell2 + sell7 + sell9 + sell11 + sell15 + sell20 + sell24) * 86.3
fprice = (sell3 + sell14 + sell18 + sell22 + sell26 + sell30) * 96.8
pprice = (sell4 + sell12 + sell21 + sell27) * 135.9
tprice = (sell5 + sell13 + sell16 + sell19 + sell23 + sell25 + sell29) * 65.8
cprice = sell6 * 49.3
zprice = yprice + nprice + fprice + pprice + tprice + cprice

print("羽绒服的销售占比：",round(((sell1 + sell8 + sell10 + sell17 + sell28) / zsell * 100),2),'%')
print("牛仔裤的销售占比：",round(((sell2 + sell7 + sell9 + sell11 + sell15 + sell20 + sell24) / zsell * 100),2),'%')
print("风衣的销售占比：",round(((sell3 + sell14 + sell18 + sell22 + sell26 + sell30) / zsell * 100),2),'%')
print("皮草的销售占比：",round(((sell4 + sell12 + sell21 + sell27) / zsell * 100),2),'%')
print("T恤的销售占比：",round(((sell5 + sell13 + sell16 + sell19 + sell23 + sell25 + sell29) / zsell * 100),2),'%')
print("衬衫的销售占比：",round((sell6 / zsell * 100),2),'%')
print("---------------------------------------------------")
print("羽绒服的销售额占比：",round((yprice / zprice * 100),2),'%')
print("牛仔裤的销售额占比：",round((nprice / zprice * 100),2),'%')
print("风衣的销售额占比：",round((fprice / zprice * 100),2),'%')
print("皮草的销售额占比：",round((pprice / zprice * 100),2),'%')
print("T恤的销售额占比：",round((tprice / zprice * 100),2),'%')
print("衬衫的销售额占比：",round((cprice / zprice * 100),2),'%')
print("---------------------------------------------------")
print("本月总销售额为：",round(zprice,2),"元")