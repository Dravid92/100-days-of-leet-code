numbers =[2,3,4]

target = 6
i = 0
j = len(numbers) - 1
while i<j:
    if numbers[i]+numbers[j] == target:
        print([i+1,j+1])
        break 
    elif numbers[i]+numbers[j]< target:
        i += 1
    else:
        j -= 1
        
        #nehamalvia

        





