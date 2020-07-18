nums = [1,2,3,4,4,3,2,1]
n = 4
new = []
for i in nums[:n]:
    new.append(i)
    new.append(nums[n])
    n+=1
print(new)
