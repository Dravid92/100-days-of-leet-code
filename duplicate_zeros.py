arr = [1,0,2,3,0,4,5,0]
n = 0
while n < len(arr):
    if arr[n] == 0:
        arr.pop(-1)
        arr.insert(n,0)
        n += 1
        
    n += 1
print(arr)