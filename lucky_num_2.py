arr = [1,2,2,3,3,3]
dic = {i:arr.count(i) for i in arr}
res = []
for key, value in dic.items():
    if key == value:
        res.append(key)
if len(res) == 0:
    print(-1)
else:
    print(max(res))

