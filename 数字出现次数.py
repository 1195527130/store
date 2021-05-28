li = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]

# print("输入q退出！")
# while True :
#     i = 0
#     count = 0
#     a = input("请输入想要查询的数字：")
#     if a == 'q':
#         print("下次再见！")
#         break
#     while i < len(list) :
#         if li[i] == int(a) :
#             count = count + 1
#         i = i + 1
#     print("数字",a,"出现了",count,"次！")

for i in range(0,len(li)):
    count = 0
    if li[i] in li[:i] :
        continue
    for j in range(0,len(li)):
        if li[i] == li[j] :
            count = count + 1
    print(li[i],"出现了",count,"次！")