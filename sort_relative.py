arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
k = 0
dic = {i:arr1.count(i) for i in arr2}
res = []
for i in dic:
    n = dic.get(i)
    for j in range(n):
        res.append(i)
dif = [a for a in arr1 if a not in arr2]
dif.sort()
res = res + dif
print(res)