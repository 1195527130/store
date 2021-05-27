a = int(input("请输入三角形的层数："))
i = 1
while i <= a :
    j = 1
    k = 1
    while k <= (a-i) :
        print(" ",end="")
        k = k + 1
    while j <= i :
        print("* ",end="")
        j = j + 1
    print()
    i = i + 1