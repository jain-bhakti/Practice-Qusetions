s = "bbbbb"

charset = set()
l = 0
res = 0
for r in range(len(s)):
    while s[r] in charset:
        charset.remove(s[l])
        l += 1
    charset.add(s[r])
    res = max(res,r-l+1)

print(res)

def my_code(s):
    string = ""
    for c in s:
        if c not in string:
            string += c

        start = 0
        end = len(string)

    while(start<=end):

        if string[start:end] in s:
            count = len(string[start:end])
            break

        else:
            start += 1

    return(count)
        