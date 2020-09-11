mat =[[5]]
#00 , 11 , 22 , 33 , 0n-1,1n-2,2n-3,3n-4
n = int(len(mat))
# left to right diagonal
lr = 0
rl = 0
if n == 1:
    print(mat[n-1][n-1])
for i in range(n):
    lr += mat[i][i]
    rl += mat[i][n-(i+1)]
if n%2 == 0:
    print(lr+rl)
else:
    print(lr+rl-mat[n//2][n//2])  # 3x3 - 11 # 5x5 - 22 #7x7 33

right to left 
