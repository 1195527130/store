a = [1,2,3,4,5,6,7,8,9]
# a = list(reversed(a))
# print(a)
for i in range(0,len(a)//2) :
    b = a[i]
    a[i] = a[len(a)-i-1]
    a[len(a)-1-i] = b
    i = i + 1
print(a)