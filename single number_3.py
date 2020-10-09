nums = [1,2,1,3,5,2]
dic = {}
for i in nums:
    if i in dic:
        del dic[i]
    else:
        dic[i] = 1
print(dic.keys())