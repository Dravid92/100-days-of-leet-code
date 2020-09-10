s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
k = 0
dic = {i:s[n] for n,i in enumerate(indices)}
fin = ''
for i in range(len(indices)):
    fin += dic[i]
    
print(fin)
