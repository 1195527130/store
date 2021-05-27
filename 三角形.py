a = int(input("请输入三角形第一条边："))
b = int(input("请输入三角形第二条边："))
c = int(input("请输入三角形第三条边："))
if a + b > c and a + c > b and b + c > a :
    if a == b == c :
        print("构成等边三角形")
    elif a == b or b == c or c == a :
        print("构成等腰三角形")
    elif a * a + b * b == c * c or b * b + c * c == a * a or c * c + a * a == b * b :
        print("构成直角三角形")
    else :
        print("构成普通三角形")
else :
    print("不能构成三角形")