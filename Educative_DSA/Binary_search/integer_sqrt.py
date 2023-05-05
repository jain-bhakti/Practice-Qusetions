#Naive Approach
def integer_square_root(k):
    res = 0
    for i in range(k):
        if i*i < k:
            res = i
    return res


#Binary Search Approach
def integer_sqrt(k):
    
    low = 0
    high = k 

    while low <= high:
        mid = (low + high) // 2
        mid_squared = mid * mid

        if mid_squared <= k:
            low = mid + 1
        else:
            high = mid - 1
    return low - 1

k = 12
print(integer_square_root(k))
print(integer_sqrt(k))
