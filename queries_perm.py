queries = [3,1,2,1]
m = 5
p = [] #12345 - q -index
fin = []

for i in range(1,m+1): # creates array based on m
    p.append(i)
# print(p)
r = p[:] #copy
for n in range(len(queries)): 
    temp = queries[n] # elements of queries 
    for q,k in enumerate(p): # change p
        if temp == k:
            fin.append(q)
            r.pop(q)
            r[0:0] = [k]

print(fin)
