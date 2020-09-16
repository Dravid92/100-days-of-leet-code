groupSizes = [3,3,3,3,3,1,3]
arr = []
for i in list(set(groupSizes)):
    temp = []
    for n,j in enumerate(groupSizes):
        if i == j:
            temp.append(n)
        if len(temp)== i:
            arr.append(temp)
            temp = []
    arr.append(temp)
print(arr)





