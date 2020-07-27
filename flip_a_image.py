A = [[1,1,0],[1,0,1],[0,0,0]]
hori = [i[::-1] for i in A]
print(hori)

for n,i in enumerate(hori):
    for k, j in enumerate(i):
        if j ==1:
            hori[n][k] = 0
        else:
            hori[n][k] = 1
print(hori)

