nums = [3,4,5,2]
i = max(nums)
nums.pop(nums.index(i))
j = max(nums)
algo = (i-1)*(j-1)
print(algo)