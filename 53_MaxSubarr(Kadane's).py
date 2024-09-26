nums = [-2,1,-3,4,-1,2,1,-5,4]
maxsum = nums[0]
cursum = 0

for n in nums:
    if cursum < 0:
        cursum = 0

    cursum += n
    maxsum = max(maxsum,cursum)

print(maxsum)