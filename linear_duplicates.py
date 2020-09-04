nums = [4,1,2,1,2]
for n,i in enumerate(nums):
    k = nums.count(i)
    if k == 1:
        print(i)