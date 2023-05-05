import math
 
def highestPowerof2(n):
 
    p = int(math.log(n, 2))
    return int(pow(2, p))

def max_power(n):
    max_pow = 0
    for i in range(n):
        pow  = 2**i
        if pow <=n and pow>max_pow:
            max_pow = pow
    return max_pow

n = 10
#print(max_power(n))
print(highestPowerof2(n))