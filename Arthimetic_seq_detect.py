arr = [3,5,1]
arr = sorted(arr)
i = 0
j = 1
for _ in range(0,len(arr)+1):
        diff = arr[1] - arr[0]
        c = 0
        if arr[j] - arr[i] == diff:
            c += 1
            if len(arr) == c:
                print(True)
            else:
                print(False)
                
            
            
            

             
        





