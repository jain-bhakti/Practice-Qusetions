s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

s = [] 
t = []
u = []   
res = []
for i in range(0,len(s1)):  
     
    for j in range(i,len(s1)):  
        s.append(s1[i:(j+1)])

for i in range(0,len(s2)):  
   
    for j in range(i,len(s2)):  
        t.append(s2[i:(j+1)])

for i in range(0,len(s3)):  
    for j in range(i,len(s3)):  
        u.append(s1[i:(j+1)])

for i in range(len(u)):
    if i %2 == 0:
        if u[i] in s:
            res.append(True)
        else:
            res.append(False)

    else:
        if u[i] in t:
            res.append(True)
        else:
            res.append(False)