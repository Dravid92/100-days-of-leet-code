t = 'test.e.mail+bob.cathy@leetcode.com'
left = "".join(t.rsplit("+",1)[:1])
# domain = "@"+ "".join(left.rsplit("@",1)[1:])
print(left)