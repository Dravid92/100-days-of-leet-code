words = ["cat","bt","hat","tree"]
chars = "atach"
res = 0
nwords = 0
nchars = 0

for i in words:
    temp = chars
    for j in i:
        if j in temp:
            nwords += 1
            temp = temp.replace(j,"",1)
    if nwords == len(i):
        res += len(i)




print(res)
