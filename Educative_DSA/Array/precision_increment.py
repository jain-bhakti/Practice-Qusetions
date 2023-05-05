A = [1, 4, 9]
s = ''.join(map(str, A))
print(int(s) + 1)


def increment(A):
    A[-1] += 1
    for i in range(len(A)-1,-1,-1):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)

    return A

print(increment(A))