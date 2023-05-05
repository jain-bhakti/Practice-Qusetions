def findKthPositive(arr, k):
    i = 1
    result = []
    while len(result)<k:
        if i not in arr:
            result.append(i)
        i += 1
    return result[-1]

def Find_Kth(arr,k):
    #check whether the first element is greater than k
    if arr[0] > k:
        return k

    #initialize two pointer point left and right bound
    l,r = 0,len(arr)-1

    #iterate till l<=r
    while l<=r:
        #calculate mid
        mid = (l+r)//2
        #check whether the difference of mid element and mid+1 <k
        if arr[mid] - (mid+1) < k:
            l = mid + 1
        else:
            r = mid - 1

    return l+k

arr = [2,3,4,7,11]
k = 5
arr = [1,2,3,4]
k = 2
print(findKthPositive(arr,k))
print(Find_Kth(arr,k))