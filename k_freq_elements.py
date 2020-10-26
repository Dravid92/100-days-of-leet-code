S = "abcd"
indexes = [0, 2]
sources = ["ab","ec"]
targets = ["eee","ffff"]
for n,i in enumerate(sources):
    if S.index(i) == indexes[n]:# abcdefg
        S = S.replace(sources[n],targets[n],1)
print(S)
