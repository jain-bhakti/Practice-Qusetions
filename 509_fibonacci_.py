n = 4

n1 = 0
n2 = 1
sum = 0
if n<=0:
    print("invalid")

else:
    for i in range(n):
        
        n1 = n2
        n2 = sum
        sum = n1+n2
    print(sum)