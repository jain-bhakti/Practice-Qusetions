#code
def duplicate_char(s):
    visited = ""
    res = []
    for c in s:
        if c not in visited:
            visited += c
        else:
            res.append(c)
    return res
    
def duplicate_count(s):
    dic = {}
    for ch in s:
        if ch not in dic:
            dic[ch] = 1 
        else:
            dic[ch] += 1 
    
    for k,v in dic.items():
        if dic[k] > 1:
            print(k , v)
        
s = "malayalam"
print(duplicate_char(s))
duplicate_count(s)
