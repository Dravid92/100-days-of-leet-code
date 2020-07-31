prices = [8,7,4,2,8,1,7,7,10,1] #[1,3,2,1,7,0,0,6,9,1]
for n,i in enumerate(prices):
  for j in prices[n+1:]:
    if i>=j:
      prices[n] = i-j
      break # this took me more than 5 hours because i forgot this statement
print(prices)