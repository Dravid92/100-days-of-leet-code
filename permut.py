nums = [1,2,3]
fin = []
def pe(nums):
    if  len(nums) == 0:
        print(fin)
    else:
        for i in range(len(nums)):
            if nums[:i]+nums[i+1:]+[nums[i]] not in fin:
                fin.append(nums[:i]+nums[i+1:]+[nums[i]])
                pe(nums[:i]+nums[i+1:]+[nums[i]])
    return fin
print(pe(nums))
            