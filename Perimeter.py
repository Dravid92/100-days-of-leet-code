grid = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
peri=0  #perimeter
for i in range(0,len(grid)):
    for j in range(0,len(grid[0])):
        cb=4 #cb=contribution, maximum of which is 4 
        if(grid[i][j]==1):
        #check if your neighbours are 1s or 0s
        #there are four neighbours total.
        #up down left and right
            if(i-1>=0 and grid[i-1][j]!=0):
            #if one cell above is 1 then it takes the uppermost egde of mine from the perimeter i contribute therefore I do minus-1
                cb-=1
            if(j-1>=0 and grid[i][j-1]!=0):
                cb-=1
            if(i+1<len(grid) and grid[i+1][j]!=0):
                cb-=1
            if(j+1<len(grid[0]) and grid[i][j+1]!=0):
                cb-=1
            peri+=cb #remember to add this contribution to the actual perimeter.
print(peri)

