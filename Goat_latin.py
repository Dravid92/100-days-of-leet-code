S = "I speak Goat Latin"
S = S.split(" ")
a ='aeiouAEIOU'
new = ''
add = 'ma'
for n,i in enumerate(S):
    if i[0] in a:
        new+= i+add
        new += (n+1) * 'a'
        new += ' '
        
    else:
        l = i[0]
        new += i[1:]+l+add
        new += (n+1) * 'a'
        new += ' '
print(new[:-1])