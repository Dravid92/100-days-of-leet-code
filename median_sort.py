# merge and sort 
# find median 
nums1 = [1,2]
nums2 = [3]
num = nums1 + nums2
num = sorted(num)
n = len(num)
if n%2 == 0:
    m1 = num[(n-1)//2]
    m2 =num[((n-1)//2)+1]
    median = float((m1+m2)/2)
else:
    median = num[(n-1)//2]
print(median)

