R = 2
C = 3
r0 = 1
c0 = 2
# fin = [[x,y] for x in range(R) for y in range(C)]
# fin.sort(key=lambda x: abs(x[0]-r0)+abs(x[1]-c0))
final = []
for i in fin:
    row = abs(r0 - i[0])
    col = abs(c0 - i[1])
    final.append([row,col])
final.sort(key = lambda x: x[0]+x[1],reverse=True)
# print(sorted([[x, y] for x in range(R) for y in range(C)], key=lambda a: abs(r0-a[0]) + abs(c0-a[1])))
print(fin)
#[[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]