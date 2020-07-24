s = "10#11#12"
splits = s.split('#')
alpha = ''
if splits[-1] == '':
    # g = splits[-1]
    # splits = splits.remove(g)
    # w = chr(int(splits[-2])+96)
    for i in splits[:-1]:
        for j in i[:-2]:
            alpha += chr(int(j)+96)
        alpha += chr(int(i[-2:])+96) # this part will change
    # alpha += w
else:
    w = ''
    for i in splits[-1]:
        w += chr(int(i)+96)
    for i in splits[:-1]:
        for j in i[:-2]:
            alpha += chr(int(j)+96)
        alpha += chr(int(i[-2:])+96)
    alpha += w
print(alpha)