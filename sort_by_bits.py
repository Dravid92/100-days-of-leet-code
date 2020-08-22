arr = [1024,512,256,128,64,32,16,8,4,2,1]
arr.sort()
ones = []
res = []
fin = []
for i in arr:
    temp = bin(i).replace("0b","")
    ones.append(str(temp).count('1'))
j = 0

res = [(arr[n],i) for n,i in enumerate(ones)]
res = sorted(res,key=lambda x:x[1])
for i in res:
    fin.append(i[0])
print(fin)

#     ones[i] = str(temp).count('1')
# fin = sorted((value,key) for key,value in ones.items())
# res = []
# for i in fin:
#     res.append(i[1])
# print(res)