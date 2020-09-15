sentence = "i love eating burger"
searchWord = "burg" # len = 4
for i in sentence:
    for j in i:
        if len(i) < len(searchWord):
            break
        else:
            word = ''
            word += j
            if len(word) == len(searchWord):
                if searchWord == i[:4]:
                    print(True)