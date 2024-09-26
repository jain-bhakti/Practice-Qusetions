s = "00110"
zero,one = s.count("0"),0              #zero = 3 one = 2
output = zero                          #output = 0
for d in s:                             # 1.d = 0 ==> zero = 2 output = 2 
    if d == "0":                        # 2.d = 0 ==> 1                 1
        zero -= 1                       # 3.d = 1 ==> 1   one = 1       1
    if d == "1":                        # 4.d = 1 ==> 1         2       1
        one += 1                        # 5.d = 0 ==> 0         2       1
    output = min(output,zero+one)

print(output)








