s = "Let's take LeetCode contest"
l = s.split(' ')
fin = ""
for i in l:
    for j in i[::-1]:
        fin += j
    fin += ' '
print(fin[:-1])
