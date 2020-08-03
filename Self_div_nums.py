left = 1
right = 22
fin = []
for i in range(left,right+1):
    if len(str(i)) == 1:
        fin.append(i)
    else:
        c = 0
        for j in str(i):
            if '0' in str(i):
                break
            if i % int(j) == 0:
                c += 1
                if c == len(str(i)):
                    fin.append(i)
                    c = 0
            else:
                break
print(fin)