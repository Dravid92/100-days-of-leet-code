nums1 = [1,2,2,3]
nums2 = [2,2]
res = []
for i in nums1:
    for j in nums2:
        if i == j:
            res.append(i)
print(list(set(res)))

# list(set(nums1)& set(nums2))