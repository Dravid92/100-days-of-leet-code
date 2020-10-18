arr = [1,2,2,6,6,6,6,7,10]

for i in arr:
    if arr.count(i)/len(arr) > 0.25:
        print(i)
        break
