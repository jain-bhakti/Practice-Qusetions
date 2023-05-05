import math
nums = [9,3,1,2,6,3] 
k = 3
count = 0
subset = [[]]
for i in range(len(nums)):
    g = nums[i]
    for j in range(i,len(nums)): 
        g = math.gcd(g,nums[j])
        if g == k:
            count += 1

print(count)

