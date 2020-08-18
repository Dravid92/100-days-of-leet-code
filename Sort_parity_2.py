A = [4,2,5,7]
even = []
odd = []
fin = []
e = 0
o = 1
for i in A:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
fin = even + odd
for i in even:
    A[e] = i
    e += 2
for j in odd:
    A[o] = j
    o +=2

print(fin,m)



