S = "abbaca"
k = 0
l = 1
t = True
count = 0
while t: # loop as to go untill no duplicates
    if l == count:  # break statement when loop has no duplicates
        break
    if S[k] == S[l]:
        S = S.replace(S[k:l+1],"") # duplicates get removed
        count = len(S) 
        k = 0 # to keep going back to strings
        l = 1
        if len(S)==0: # empty string 
            print("") # then return this
    else:
        k += 1
        l += 1
print(S)