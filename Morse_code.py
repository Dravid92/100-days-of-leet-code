morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
alpha = [chr(i) for i in range(ord('a'),ord('z')+1)]
dic = {alpha[i]:morse[i] for i in range(len(morse))}
word = ["gin", "zen", "gig", "msg"]
mor = ''
for n,i in enumerate(word):
    j = 0
    mor += dic.get(i[j])
    if j < len(i):
        j += 1
    # print(n,i)
    if len(word) == n +1 :
        res = [''.join(mor[k:k+ len(i)]) for k in range(0,len(mor),len(i))]
        out = len(set(res))
print(out)

# Short version : 

# seen = {"".join(morse[ord(c) - ord('a')] for c in word)
                # for word in words}
# print(len(seen))