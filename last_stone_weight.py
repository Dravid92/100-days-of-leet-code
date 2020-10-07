stones = [2,7,4,1,8,1]
for i in range(len(stones)):
    if len(stones) <= 1:
        break
    else:
        y = stones.pop(stones.index(max(stones)))
        x = stones.pop(stones.index(max(stones)))
        # print(x,y)
        if x!=y:
            stones.append(y-x)
if len(stones) == 0:
    print(0)
else:
    print(stones[0])      

