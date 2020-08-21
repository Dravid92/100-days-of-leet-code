s  = ["h","e","l","l","o"]
l  = len(s)
n = int(l//2)
j = -1
if l%2 == 0:
    for i in range(n):
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        j -= 1
else:
    for i in range(n):
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        j -= 1
print(S)