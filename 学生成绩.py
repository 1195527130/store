students = [
    {'name':'张三','age':23,'score':88,'tel':'23423532','gender':'男'},
    {'name':'李四','age':26,'score':80,'tel':'12533453','gender':'女'},
    {'name':'王五','age':15,'score':58,'tel':'56453453','gender':'男'},
    {'name':'赵六','age':16,'score':57,'tel':'86786785','gender':'保密'},
    {'name':'小明','age':18,'score':98,'tel':'23434656','gender':'女'},
    {'name':'小红','age':23,'score':72,'tel':'67867868','gender':'女'},
]

count = 0
failstu = {}
for index,value in enumerate(students) :
    if value.get('score') < 60 :
        count = count + 1
        failstu[value.get('name')] = value.get('score')
print("成绩不及格的有",count,"个学生！")
print("-----------------------------------")
print("不及格的学生名单为：",failstu)
print("-----------------------------------")
count1 = 0
for index,value in enumerate(students) :
    if value.get('age') < 18 :
        count1 = count1 + 1
print("未成年的有",count,"个学生！")
print("-----------------------------------")
print("手机号尾数为8的学生有：",end='')
for index,value in enumerate(students) :
    if int(value.get('tel')) % 10 == 8 :
        print(value.get('name'),"\t",end='')
print()
print("-----------------------------------")
stu = ''
for i in range(0,len(students)) :
    for j in range(i + 1,len(students)) :
        if students[i].get('score') < students[j].get('score') :
            a = students[i]
            students[i] = students[j]
            students[j] = a
print("最高分为：",students[0].get('score'),"，他的名字为：",students[0].get('name'))
print("-----------------------------------")
print("重新排序后的列表为：")
for index,value in enumerate(students) :
    print(value)
print("-----------------------------------")
for index,value in enumerate(students) :
    if value.get('gender') == '保密' :
        students.remove(value)
print("删除性别为保密的学生后的列表为：")
for index,value in enumerate(students) :
    print(value)
print("-----------------------------------")













