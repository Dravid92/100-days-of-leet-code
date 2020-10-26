coordinates = [[-3,-2],[-1,-2],[2,-2],[-2,-2],[0,-2]]
# they have same scale of increment on x and y 
# one of the coordinate is a constant 

coordinates = sorted(coordinates)
print(coordinates)

xd = []
yd = []
countx = 0
county = 0
for i in range(len(coordinates)-1):
    xd.append((coordinates[i+1][0] - coordinates[i][0])**2)
    yd.append((coordinates[i+1][1] - coordinates[i][1])**2)

t = set(xd)
y = set(yd)
print(list(y)[0])
if len(t) == 1:
    if list(t)[0] == 0:
        print(True)
    if list(y))[0] == 0:
        print(True)
if len(t) == 1:
    if len(y) == 1:
        print(True)
    else:
        print(False)
else:
    print(False)





