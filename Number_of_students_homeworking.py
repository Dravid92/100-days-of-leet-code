count = 0
    # i = 0 
    for i in range(0,len(startTime)):
        if queryTime >= startTime[i] and queryTime <= endTime[i]:
            count += 1
        # else: 
        #     i += 1
    return count
       
                