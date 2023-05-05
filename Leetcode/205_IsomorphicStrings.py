s = "egg"
t = "add"
count_s = 0
count_t = 0
result = False
if len(s) == len(t):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count_s += 1

        if t[i] == t[i+1]:
            count_t += 1

        if count_s == count_t:
            result = True
        else:
            result = False

print(result)


