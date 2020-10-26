light = [2,1,3,5,4]
res = {i:'o' for i in range(len(light))} # 'o' 'n' 'b'
count = 0
for n,i in enumerate(light):
    res[i-1] = 'n'
    

