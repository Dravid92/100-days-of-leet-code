# how to convert nums to bi
# complement 
# bi to nums
nums = 5
bi = bin(nums).replace("0b","")
compliment = ''
for i in str(bi):
    if i == '0':
        compliment += '1'
    else:
        compliment += '0'
print(int(compliment,2))

