s = "dvdf"
temp = ''
count = []
if len(s) == 0: # no input
    print(0)
elif s == ' ': # if the input is just space
    print(len(s))
else: # usual case
    for i in s:
        if i not in temp:
            temp += i
            count.append(len(temp))
        else:
            temp = temp[temp.index(i)+1:]
            temp += i
            count.append(len(temp))
    print(max(count))
