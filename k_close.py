points = [[1,3],[-2,2]]
K = 1
#sqrt((x1-x2)**2 + (y1-y2)**2)
x1 = 0
y1 = 0
dic = {}
for i in enumerate(points):
    x2 = i[0]
    y2 = i[1]
    dis = (x1 - x2)**2 + (y1-y2)**2
    dic[i] = dis
print(dic)
    
