A = [2,7,4]
K = 181
s = ''
for i in A:
    s += str(i)
res1 = int(s) + K
res2 = []
for j in str(res1):
    res2.append(int(j))
print(res2)
