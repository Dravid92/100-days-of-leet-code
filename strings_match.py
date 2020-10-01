words = ["leetcode","et","code"]
res = []
for n,i in enumerate(words):
    for j in words:
        if i != j:
            if i in j:
                res.append(i)

print(list(set(res)))
