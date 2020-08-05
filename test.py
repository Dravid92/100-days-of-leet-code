# li = [14,15,16]
# l2 = [15,14,16]
# if l2!= li:
#     print('true')
# res = []
# left = 1
# right = 22
# for i in range(left, right+1):
#     if str(i)[-1] == '0':
#         break
#     else:
#         res += [i for j in str(i) if i%int(j) == 0]

# print(li)

dic = {1: 1, 2: 1, 3: 2}
for key,value in dic.items():
    if value >1:
        print(key)
# print(dic.get(2))
    