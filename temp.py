# This problem exceeded the time , but the output is the right one!

T = [73, 74, 75, 71, 69, 72, 76, 73]
res = []
for m,i in enumerate(T):
    count = 0
    for j in T[m:]:
        if j >i:
            res.append(T[m:].index(j) - T[m:].index(i))
            count += 1
            break
        else:
            if m == len(T)-1:
                res.append(0)
                count += 1
    if count == 0:
        res.append(0)
        
print(res)

