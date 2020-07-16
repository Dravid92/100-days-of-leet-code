a = [1,2,3,4]
s =0
sum = []
for index,i in enumerate(a):
    s += a[index]
    sum.append(s)

    print(index,i)

print(sum)
    