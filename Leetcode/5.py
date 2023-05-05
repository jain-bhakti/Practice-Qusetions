def solution_n2(s):
    palin = []
    for i in range(len(s)+1):
        for j in range(i+1,len(s)+1):
            
            if s[i:j] == "".join(reversed(s[i:j])):
                palin.append(s[i:j])
                
    length = 0
    for i in palin:
        length = max(length,len(i))

    for i in palin:
        if len(i) == length:
            print(i)
            break

def optimised(s):
    pass 

s = "babaadaa"
solution_n2(s)
