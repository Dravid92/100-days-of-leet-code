S = 'IDID'
lo = 0
hi = len(S)
fin = []
for n,i in enumerate(S):
    if i == 'I':
        fin.append(lo)
        lo += 1
    else:
        fin.append(hi)
        hi -= 1
return fin + [lo]
# solution checked
        