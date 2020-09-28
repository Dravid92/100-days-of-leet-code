products = ["mobile","mouse","moneypot","monitor","mousepad"]

searchWord = "mouse"
res = []
#[["baggage","bags","banner"],["baggage","bags","banner"]
#,["baggage","bags"],["bags"]]
n = 1
for n,i in enumerate(searchWord):
    temp = []
    for k,j in enumerate(sorted(products)):
        if n < len(searchWord):
            if searchWord[:n+1] == j[:n+1]:
                temp.append(j)
                if len(temp) >= 3:
                    res.append(temp)
                    break
                else:
                    if k == len(products) -1:
                        res.append(temp)
            else:
                if k == len(products) -1:
                    res.append(temp)
print(res)                






