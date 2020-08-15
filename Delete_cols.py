A = ["dmdbhshl","hqzeweju","wxnnjnvy"]
 # To find out the mini number of characters to be removed 
 # so that the order of the strings are increasing in order
arr = {}
fin = []
for i in A:
    for j in range(0,len(i)):
        arr.setdefault(j,[]).append(i[j]) # appends the value based on the index
for i in arr:
    if sorted(arr.get(i)) != arr.get(i): # compares whether the values are in increasing order 
        fin.append(i) # if not the index gets appended here 
print(len(fin))
