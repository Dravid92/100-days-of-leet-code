n = 2
m = 3
indices = [[0,1],[1,1]]
# create zero matrix with n and m dim
# loop through indices 
# [idx] - [0,1] - i =0 ==> [i][m]
# increment only rows first and then colum
mat = [[0 for i in range(m)] for j in range(n)]
for i in indices:
    for j in range(len(mat[i[0]])):
        mat[i[0]][j] += 1
tra = [[row[i] for row in mat]for i in range(len(mat[0]))]
for i in indices:
    for j in range(len(tra[i[1]])):
        tra[i[1]][j] += 1
count = 0
for i in tra:
    for j in i:
        if j%2 != 0:
            count += 1
print(count)