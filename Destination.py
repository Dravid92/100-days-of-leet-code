paths = [["B","C"],["D","B"],["C","A"]]
k = {path[0]:path[1] for path in paths}
s = [paths[0][0]]
while True:
    c  = s.pop()
    if c not in k:
        break
    else:
        s.append(k[c])
print(c)
# credits : Abedin022
# so,  the problem is to find the element that does not have a start 