b = [1,1,3,5,2,1,5,2,1,5,3,5,6,9,7,4,7,1,9]

def num_count(li) :
    count = {}
    for index,value in enumerate(li) :
        if value in li[:index] :
            count[value] = count.get(value) + 1
        else :
            count[value] = 1
    return count

a = num_count(b)
print(a)