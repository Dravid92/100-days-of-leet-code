a = [0,1,2,0]
# [3,2,1,0]
# for i in range(0,len(a)):
#     temp = a[i]
#     a[i] = a[-i-1]
#     a[-1-i] = temp
if max(a[len(a)//2:]) == a[len(a)//2:][0]:
            m = a[len(a)//2:][0]
print(a.index(m))