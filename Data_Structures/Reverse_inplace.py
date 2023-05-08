#python string class objects are immutable hence using a list of characters to reverse inplace.

def reverse_inplace(s):
    l = 0
    h = len(s)-1
    while l<h:
        s[l],s[h]=s[h],s[l]
        l += 1 
        h -= 1 
    return s
    
s = ["r","e","v","e","r","s","e","m","e"]
print(reverse_inplace(s))
