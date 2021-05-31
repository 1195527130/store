li = [1,2,7,9,5,8,4,6,3,5]

for i in range(0,len(li)) :
    for j in range(i + 1,len(li)) :
        if li[i] < li[j] :
            a = li[i]
            li[i] = li[j]
            li[j] = a
print(li)