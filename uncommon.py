A = "fv kisxg hfmeq fw gi fpyc ojtr s hfmeq ojtr kisxg"

B = "chpi hfmeq chpi dq hwtxa orql orql m s fw dq m fw"
a = A.split(" ")
b = B.split(" ")
fin = list(set(a)- set(b)) + list(set(b)- set(a))
s = []
for n,i in enumerate(fin):
    if a.count(i) > 1:
        s.append(i)
    if b.count(i) > 1:
        s.append(i)

print(list(set(fin)-set(s)))