text = "loonbalxballpoon"
word = "balloon"
count = 0
temp = ""
for i in range(len(word)):
    if word[i] in text:
        temp += word[i]
        text.replace(word[i],"",1)
        if temp == word:
            count += 1
print(count)


    