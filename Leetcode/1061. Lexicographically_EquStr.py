s1 = "parker"
s2 = "morris"
baseStr = "parser"
res = ""

table = dict()
print(table)
for i in s1:
    table[i] = []

for i in s2:
    table[i] = []
   
for i in range(len(s1)):
    if s1[i] in table:
        table[s1[i]].append(s2[i])

for i in range(len(s1)):
    if s2[i] in table:
        table[s2[i]].append(s1[i])


for i in range(len(baseStr)):
    
    

for i in baseStr:
    if i in table:
        res += min(min(table[i]),str(i))

if "r" in res:
    res.replace("r","k")

print(table)
print(res)