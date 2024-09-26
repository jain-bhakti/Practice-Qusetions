def CountBits(n):
    count = 0
    for i in range(1,n+1):
        count += SetBits(i)

    return count

def SetBits(x):
    if x <= 0:
        return 0

    return (0 if int(x%2)==0 else 1) + SetBits(int(x/2))


def Bitwise_solution(n):
    


n = 5
print(CountBits(n))