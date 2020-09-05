grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]

# for a buildings height to be raised
    # check row max
    # check column max
    # get minimum of both 
    # increase the height to the minimum
    # or find the difference between each element and
    # the minimum and add 


for i in grid:
     row_max.append(max(i))

grid2 = list(map(list,zip(*grid)))

for j in grid2:
    col_max.append(max(j))
fin = 0
for n,i in enumerate(row_max):
    for q,k in enumerate(col_max):
        su = min(i,k)
        fin += su-grid[n][q]
print(fin)
