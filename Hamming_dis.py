x = 1 #0001
y = 4 #0100 diff = 101 which can be obtained by xor operator 
# for positional diff count 1s
ans = x^y # xor between the two numbers
print(str(bin(ans)[2:].count('1'))) 
#or 
ans = int(bin(x)[2:]) +int(bin(y)[2:])
print(str(ans).count('1'))
#convert the xor to binary and count the 1s

# credits : vivek1mishra
