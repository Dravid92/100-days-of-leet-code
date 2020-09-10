arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3
p = 0
# credits - The shubham99
l = int(len(arr))
for i in range(0,l-2):
    for j in range(i+1,l-1):
        if abs(arr[i] - arr[j]) <= a: # early stopper 
            for k in range(j+1,l):
                if abs(arr[j] - arr[k]) <= b:
                    if abs(arr[i] - arr[k]) <= c:
                        p += 1
                
print(p)
