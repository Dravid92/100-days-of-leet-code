arr = [1,1,1]
i = 0
j = 1
k = 2
while k <len(arr):
    if arr[i]%2 != 0:
        if arr[j]%2 != 0:
            if arr[k]%2 != 0:
                print(True)
                i += 1
                j += 1
                k += 1
            else:
                i += 1
                j += 1
                k += 1
        else:
                i += 1
                j += 1
                k += 1
    else:
                i += 1
                j += 1
                k += 1
print(False)
            