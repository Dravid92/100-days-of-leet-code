n = 4
ans = [k for k in range(0,n)]
if n == 1:
    ans = [0]
    print(ans)
else:
    if n%2 == 1:
        for i in range(0,n//2+1):
            ans[i] = -1*(n//2-i)
            ans[n-i-1] = (n//2-i)
    else:
        for i in range(0,n//2):
            ans[i] = -1*(n//2-i)
            ans[n-i-1] = (n//2-i)
print(ans)
