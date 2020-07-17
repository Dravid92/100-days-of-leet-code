a = [1,2,3,1,1,3]
# array for testing
count = 0
# intial counts of good pair
for i in range(0,len(a)) :
    for j in range(1,len(a)):
        #for comparison of the elements of array
        if i < j:
            # so that the loop doesn't compare from the start
            if a[i] == a[j]:
                # condition 
                count += 1
                # good pair count up
print(count)