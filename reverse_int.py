x = -123
res = ''
for i in range(len(str(x)),1,-1):
    if x < 0:
        res += '-'
        x = abs(x)
    elif x%10 == 0:
        x = x//10
    res += str(x)[i-1]

print(2**31)