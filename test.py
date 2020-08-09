a = [0,1,2,3]
# [3,2,1,0]
# for i in range(0,len(a)):
#     temp = a[i]
#     a[i] = a[-i-1]
#     a[-1-i] = temp

a[3:] = a[:2:-1]
print(a)