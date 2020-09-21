lo = 7
hi = 11
k = 4
arr = []
fin = {}
def fun(x):

    if x == 1:
        fin[i] = len(arr)
    elif x%2 == 0:
        x = x/2
        arr.append(x)
        return fun(x)
    else:
        x = 3*x+1
        arr.append(x)
        return fun(x)
for i in range(lo,hi+1):
    arr = []
    fun(i)
l = sorted(fin,key = fin.get)
print(l[k-1])