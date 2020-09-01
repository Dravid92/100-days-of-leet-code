arr = [4,3,1,2]
 #credits ===  man_it
arr.sort()
mini=min(arr[i]-arr[i-1] for i in range(1,len(arr)))
print([[arr[i-1],arr[i]] for i in range(1,len(arr)) if arr[i]-arr[i-1]==mini])
