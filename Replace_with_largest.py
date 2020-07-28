arr = [17,18,5,4,6,1]
# piv = arr[len(arr)/2]
k = 1
for n,i in enumerate(arr):
    if k <= len(arr)- 1:
        ma = max(arr[k:]) 
        arr[n] = ma
        k += 1
arr[-1] = -1
print(arr)

