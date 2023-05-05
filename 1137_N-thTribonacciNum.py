#recursive Solution
""" Recursive solution reuires etra tiem for function call stack and hence we need to apply dynamic programming concepts"""

def tribonacci(n):
    if n==0:
        return 0

    if n==1 or n==2:
        return 1

    return tribonacci(n-3)+tribonacci(n-2)+tribonacci(n-1)

#Iterative Solution
"""Takes lesser time as all the previous results are stored and need not to be recalculated. Hence uses 
Dynamic programming concepts"""

def tribonacci_itr(n):
    res = [0,1,1]+[0]*35

    for i in range(3,n+1):
        res[i] = res[i-1]+res[i-2]+res[i-3]
    return res[n]


n = 30
print(tribonacci_itr(n))