def find_closest(A,target):
    min_diff = min_left = min_right = float("inf")
    closest = None
    low = 0
    high = len(A)-1

    if len(A) == 0:
        return None
    if len(A) == 1:
        return A[0]
    else:
        while low<=high:
            mid = (low+high)//2

            if mid+1 < len(A):
                min_right = abs(A[mid + 1] - target)
            if mid > 0:
                min_left = abs(A[mid - 1] - target)

            if min_left<min_diff:
                min_diff = min_left
                closest = A[mid-1]

            if min_right<min_diff:
                min_diff = min_right
                closest = A[mid+1]

            if target < A[mid]:
                high = mid-1
                if high < 0:
                    return A[mid]

            elif target>A[mid]:
                low = mid+1
                
            else:
                return A[mid]
        return closest

A1 = [1, 2, 4, 5, 6, 6, 8, 9]
target = 0
print(find_closest(A1,target))         