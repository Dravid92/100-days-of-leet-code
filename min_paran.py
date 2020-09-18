S = "()))((" # for every left out closed paran ,
#  is the needed open paran

# credit - coder93

count = 0
inv = 0
for i in S:
    if i == '(':
        count += 1
    else:
        if count != 0: # there is an open paran
            count -= 1 # parantheses is in balance
        else: # count = 0 , there an invalide closed paran
            inv += 1 # invalid closed parentheses , without open
    
if count != 0: # whether there are invalid open paran
    inv += count


print(inv)