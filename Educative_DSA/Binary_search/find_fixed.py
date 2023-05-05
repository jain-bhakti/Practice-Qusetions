def find_fixed(A):
    low = 0
    high = len(A)-1
    while low<=high:
        mid = (low+high)//2
        if A[mid] < mid:
            low = mid+1
        elif A[mid] > mid:
            high = mid-1
        else:
            return A[mid]
    return None


A1 = [-10, -5, 0, 3, 7]
A2 = [0, 2, 5, 8, 17]
A3 = [-10, -5, 3, 4, 7, 9]
print(find_fixed(A2))
