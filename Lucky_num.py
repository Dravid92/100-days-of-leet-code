matrix = [[7,8],[1,2]]
minn = []
maxx = []
res = []
for i in matrix:
    minn.append(min(i))
trax = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
for i in trax:
    maxx.append(max(i))
for k in minn:
    for l in maxx:
        if k == l :
            res.append(k)
print(res)