s = "aabb"
dic = {}
l = []
index = 0
for i in s:    
	if i not in dic:  
		dic[i] = 0
            
for i in s:
        dic[i] +=1
            
for i in dic:
	if dic[i] == 1:
		l.append(i)
		break
	
if not l:
	print(-1)
else:
	index = s.index(l[0])
	print(index)
