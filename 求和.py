a = [0]*10
i = 0
while i < 10 :
    a[i] = int(input("输入一个数："))
    i = i + 1

print("总和为：",sum(a))
print("最大值为：",max(a))
print("平均值为：",(sum(a)/10))