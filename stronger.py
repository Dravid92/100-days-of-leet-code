# sort elements in ascending -find the median
# sort the elements based on the difference bet elem and median

#credits = coder93

arr = [1,1,3,5,5]
k = 2
arr = sorted(arr)
n = len(arr)

m = arr[(n-1)//2]
l , r = 0,n-1
res = []
count = 0
while l <=r:
    if abs(arr[r]-m) >= abs(arr[l]-m):
        res.append(arr[r])
        r -= 1
    elif abs(arr[l]-m) > abs(arr[r]-m):
        res.append(arr[l])
        l += 1
    count +=1
    if count == k:
        print(res)


    


    
    





    

