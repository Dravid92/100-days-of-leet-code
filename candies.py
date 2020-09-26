candies = 10
num_people = 3
people = [0 for i in range(num_people)]

n = 0
m = 1
while candies > 0:
    if n < len(people):
        if m > candies:
            people[n] += candies
            break
        else:
            people[n] += m
            candies = candies - m
            n += 1
            m += 1
    else:
        n = 0
        if m > candies:
            people[n] += candies
            break
        people[n] += m
        candies = candies - m
        m += 1
        n += 1
print(people)