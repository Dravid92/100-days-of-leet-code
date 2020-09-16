n = 3
arr = []
steps = 0
# create an array 
for i in range(n):
    arr.append((2*i)+1)
if n%2 == 0: # 1,3,5,7,9,11 # inserted the value to be converted to #6
    arr.insert(n//2,n) # difference between value and numbers = steps
for i in arr[:n//2]:
    steps += arr[n//2] - arr[i]

print(steps)



    

