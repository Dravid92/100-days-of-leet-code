s = "leEeetcode"
c = 0
while c < len(s)-1:
    if ord(s[c])-ord(s[c+1]) == 32:
        s = s.replace(s[c]+s[c+1],"")
        c = 0
    elif ord(s[c+1]) - ord(s[c]) == 32:
        s = s.replace(s[c]+s[c+1],"")
        c = 0
    else:
        c += 1
print(s)