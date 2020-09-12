points = [[3,2],[-2,2]]
count = 0
for o in range(len(points)): # take two points and find the diff
    if o+1 < len(points):
        if points[o] == points[o+1]:
            count += 0
        else:
            x1,x2 = points[o][0],points[o+1][0] #1,3 # 3,-1
            y1,y2 = points[o][1],points[o+1][1] #1,4 # 4,0
            if x1 != x2 or y1 != y2:
                dis1 = abs(x2-x1) # 2 # 4
                dis2 = abs(y2-y1) # 3 # 4
                count += max(dis1,dis2) # 3 + 4

print(count)

        



    
