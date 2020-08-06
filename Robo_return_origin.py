moves = 'LL'
L = 0
R = 0
U = 0
D = 0
sum = L + R + U +D
for i in moves:
    if i == 'L':
        L -= 1
    elif i == 'R':
        R += 1
    elif i == 'U':
        U -= 2
    else:
        D += 2
if sum == 0:
    print(True)
else:
    print(False)