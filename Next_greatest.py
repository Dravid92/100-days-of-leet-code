nums1 = [2,4]
nums2 = [1,2,3,4]
res = []
for n,i in enumerate(nums1):
    for j in nums2[nums2.index(i):]:
        cout = 0
        if j > i:
            res.append(j)
            cout += 1
            break 
    if cout == 0:
        res.append(-1)     
print(res)        


