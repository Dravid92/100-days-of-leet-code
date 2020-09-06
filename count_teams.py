rating = [2,5,3,4,1]
# credits - akashgkrishnan

count = 0
length = len(rating)
if length < 3:
    print(0)

for i in range(length):
    for j in range(i+1, length):
        for k in range(j + 1, length):
            if (rating[i] > rating[j] > rating[k]) or (rating[i] < rating[j] < rating[k]):
                count += 1
print(count)



