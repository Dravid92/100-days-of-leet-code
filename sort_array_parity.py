a = [3,1,2,4]
odd = []
even = []
for i in a:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
res = even + odd
print(res)
