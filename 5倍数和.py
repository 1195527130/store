a = [1,5,21,30,15,9,30,24]
i = 0
num = 0
while i < len(a) :
    if a[i] % 5 == 0 :
        num = num + a[i]
    i = i + 1
print(num)
