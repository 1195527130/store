Chinese = ['小明','小张','小黄','小杨']
Math = ['小黄','小李','小王','小杨','小周']
English = ['小杨','小张','小吴','小冯','小周']

a = []
for index,value in enumerate(Chinese) :
    a.append(value)
for index,value in enumerate(Math) :
    if value in a :
        continue
    else :
        a.append(value)
for index,value in enumerate(English) :
    if value in a :
        continue
    else :
        a.append(value)
print("总共有",len(a),"个学生选课！")
print("----------------------------------------------------------------------------------------------------")
print("总共有",len(Chinese),"个人选了第一个科目！他们的名单为：",Chinese)
print("----------------------------------------------------------------------------------------------------")
b = []
for index,value in enumerate(a) :
    if (value in Chinese and value in Math) or (value in Math and value in English) or (value in English and value in Chinese) :
        continue
    else :
        b.append(value)
print("总共有",len(b),"个人选了一个科目！他们的名单为：",b)
print("----------------------------------------------------------------------------------------------------")
c = []
for index,value in enumerate(a) :
    if value in Chinese and value in English :
        c.append(value)
print("总共有",len(c),"个人同时选了语文和英语！他们的名单为：",c)

