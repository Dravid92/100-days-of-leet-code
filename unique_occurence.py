arr = [1,2]
d = {i:arr.count(i) for i in arr}
va = sorted(list(d.values()))
un = sorted(list(set(va)))
if va  != un:
    print(False)
else:
    print(True)

