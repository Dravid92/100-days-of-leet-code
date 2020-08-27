S = "loveleetcode"
C = 'e'
 ins = []
minn = []
for n,i in enumerate(S): # loops through the string and return the index of the given letter(C)
    if i == C:
        ins.append(n) # index appended in ins
for n,i in enumerate(S):  # loop S
    temp = []
    for j in range(len(ins)): # index loop
        temp.append(abs(n-ins[j])) # gets the absoulte difference
    minn.append(min(temp))  # appends the min as output

print(minn)
        


