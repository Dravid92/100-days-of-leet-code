f = 'QqWwEeRrTtYyUuIiOoPp'
s = 'AaSsDdFfGgHhJjKkLl'
t = 'ZzXxCcVvBbNnMm'
arr = []
for n,i in enumerate(words):
    k = 0
    if i[k] in f:
        for j in i:
            if j in f:
                k += 1
                if k == len(i):
                    arr.append(i)
    elif i[k] in s:
        for j in i:
            if j in s:
                k += 1
                if k == len(i):
                    arr.append(i)
            
    else:
        for j in i:
            if j in t:
                k += 1
                if k == len(i):
                    arr.append(i)