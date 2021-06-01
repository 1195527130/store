dict = {"k1":"v1","k2":"v2","k3":"v3"}

# print("所有的键为： ",end='')
# for i in dict :
#     print(i,"\t",end='')
# print()
a = dict.keys()
print(a)
print("-------------------------")
# print("所有的值为： ",end='')
# for i in dict :
#     print(dict.get(i),"\t",end='')
# print()
b = dict.values()
print(b)
print("-------------------------")
dict["k4"] = "v4"
print("增加后所有的键值为： ",end='')
for i in dict :
    print(i,"=",dict.get(i),"\t",end='')