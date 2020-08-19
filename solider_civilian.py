mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
k = 3
arr = {n:i.count(1) for n,i in enumerate(mat)}
arr = sorted(arr.items(),key = lambda x:x[1])
print(arr)
for i in arr[:k]:
    print(i[0])