def BinarySearch(arr,target):
    low = 0 
    high = len(arr)-1
    while low<=high:
        mid = (low+high)//2
        if target == arr[mid]:
            return mid

        elif target < arr[mid]:
            high = mid-1

        else:
            low = mid+1

def BinarySearch_rec(arr,target,low,high):
    if low>high:
        return False

    else:
        mid = (low+high)//2
        if target == arr[mid]:
            print(mid)
            return True
        elif target < arr[mid]:
            return BinarySearch_rec(arr,target,low,mid-1)
        else:
            return BinarySearch_rec(arr,target,mid+1,high)    


arr = [2,3,4,5,6,7,8]
target = 2
indx = BinarySearch(arr,target)
print("{} found at {} index".format(target,indx))

print(BinarySearch_rec(arr,target,0,len(arr)-1))

#print("{} found at {} index".format(target,index))


         
