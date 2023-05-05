def Brute_force(A,target):
    for i in range(len(A)):
        for j in range(i,len(A)):
            if A[i] + A[j] == target:
                print(A[i],A[j])
                return True
    return False

def two_sum_dict(A,target):
    dt = dict()
    for i in range(len(A)):
        if A[i] in dt:
            print(dt[A[i]], A[i])
            return True
        else:
            dt[target - A[i]] = A[i]

def two_pointers(A,target):
    i = 0
    j = len(A)-1
    while i < j:
        if A[i] + A[j] == target:
            print(A[i], A[j])
            return True
        elif A[i] + A[j] < target:
            i += 1
        else:
            j -= 1
    return False

A = [-2, 1, 2, 4, 7, 11]
target = 13

print(Brute_force(A,target))
print(two_sum_dict(A,target))
print(two_pointers(A,target))
