a = 9996
array = [int(i) for i in str(a)]
ray = []
# print(array)
for j,n in enumerate(array):
    if n == 6:
        array[j] = 9
        break
print(int("".join(map(str,array))))
