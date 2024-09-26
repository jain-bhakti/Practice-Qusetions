def restore(s):
    res = []
    string = ""
    for c in s:
        string = ""
        if len(string) < 3:
            string += c
        if len(string) == 3:
            res.append(string)

    return res

s = "25525511135"
print(restore(s))
