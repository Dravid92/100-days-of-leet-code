heights = [5,1,2,3,4]
if sorted(heights) == heights:
    print(0)
s = sorted(heights)
count = 0
k = 0
for i in heights:
    for j in sorted(heights)[k:]:
        if i != j:
            count += 1
            k += 1
            break
        k += 1
        break
print(count)
