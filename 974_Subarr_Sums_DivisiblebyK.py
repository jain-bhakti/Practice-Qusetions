import math
def subarraysDivByK(nums, k):
    count = 0
    lists = [[]]
    for i in range(len(nums) + 1):
        for j in range(i):
            lists.append(nums[j: i])

            if sum(nums[j:i])%k == 0:
                count += 1

    return count

nums = [4,5,0,-2,-3,1]
k = 5
print(subarraysDivByK(nums,k))