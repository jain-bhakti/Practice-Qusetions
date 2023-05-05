def optimized(nums,target):
    low = 0
    high = len(nums)-1
    while(high >= low):
        mid = (low+high)//2
        
        if nums[mid] == target:
            return mid

        if nums[mid]<target:
            low = mid+1
        else:
            high = mid-1

    return low


def solution(nums,target):
    index = int()
    if target in nums:
        index = nums.index(target)

    else:
        for i in range(len(nums)):
            if nums[i] > target:
                index = i
                return(index)

nums = [1,3,5,6]
target = 2
result = optimized(nums,target)
print(result)

   
    

