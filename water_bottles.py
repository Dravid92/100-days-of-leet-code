numBottles = 15
numExchange = 4
def bottles(numBottles,numExchange):
    count = 0
    if numBottles < numExchange:
        return count
    if numBottles%numExchange == 0:
        count += numBottles // numExchange
        numBottles = numBottles // numExchange 
        return bottles(numBottles,numExchange)
    else:
        count += numBottles // numExchange
        numBottles = numBottles -  (numBottles // numExchange)*numExchange
        return bottles(numBottles,numExchange)
print(bottles(numBottles,numExchange))

        


