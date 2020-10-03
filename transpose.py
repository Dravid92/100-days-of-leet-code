A = [[1,2,3],[4,5,6]]
n = len(A) #2
m = len(A[0]) #3
res = []
for i in range(m):
    temp = []
    for j in range(n):
        temp += [A[j][i]]
    res += [temp]
print(res)


        


