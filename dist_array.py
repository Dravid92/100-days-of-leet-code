arr1 = [1,4,2,3]
arr2 = [-4,-3,6,10,20,30]
d = 3
count = []
for n,i in enumerate(arr1):
    temp = []
    for j in arr2:
        temp.append(abs(i-j))
    for k in temp:
        if k <= d:
            count.append(n)

print(len(arr1) - len(set(count)))