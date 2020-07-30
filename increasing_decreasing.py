s ="zaaaabbbbcccc"
arr = []

def rec(s:str,arr:list) -> str:
    if len(s) == 0 :
        return "".join(arr)
    else:
        for i in range(ord('a'),ord('z')+1):
            if chr(i) in s:
                arr.append(chr(i))
                s = s.replace(chr(i),"",1)
        for i in range(ord('z'),ord('a')-1,-1):
            if chr(i) in s:
                arr.append(chr(i))
                s = s.replace(chr(i),"",1)
    return rec(s,arr)

    Credits : naw7az
    '''
def rec(s: str, arr: list) -> str:
        if len(s) == 0:
            return "".join(arr)
        else:
            for i in range(ord("a"), ord("z")+1):
                if chr(i) in s:
                    arr.append(chr(i))
                    s = s.replace(chr(i), "", 1)
            for i in range(ord("z"), ord("a")-1, -1):
                if chr(i) in s:
                    arr.append(chr(i))
                    s = s.replace(chr(i), "", 1)
        return rec(s, arr)
'''
print(rec(s,arr))

# print(fin,ls)