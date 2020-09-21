nums = [4,3,2,7,8,2,3,1]
dic = {}
res = []
for i in nums:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
for key,val in dic.items():
    if val == 2:
        res.append(key)
return res
    #prashantpettyshetty
