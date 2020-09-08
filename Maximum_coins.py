piles = [9,8,7,6,5,1,2,3,4] #122478
n = int(len(piles)/3)
piles.sort()
me = 0
for i in range(-2,(n*-2)-2,-2):
    me += piles[i]
print(me)