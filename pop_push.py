target = [2,3,4]
n = 3
arr = ['Push','Pop']
fin = []
m = 0
for i in range(1,n+2):
    if m <= len(target)-1:
        if target[m] != i:
            for k in arr:
                fin.append(k)
        else:
            fin.append('Push')
            m += 1
print(fin)