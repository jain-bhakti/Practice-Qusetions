def singleNonDuplicate(nums):
    for i in range(len(nums)-1):
        if nums[i] != nums[i+1] and nums[i] != nums[i-1]:
            return nums[i]

def naive(nums):
    dic = {}

    for i in nums:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    for i in dic.keys():
        if dic[i] == 1:
            return i

nums = [1,1,2,3,3,4,4,8,8]
nums = [3,3,7,7,10,11,11]
print(singleNonDuplicate(nums))