def max_sum(nums):
    total = 0
    gmax,gmin = nums[0],nums[0]
    currmax , currmin = 0 , 0
    for n in nums:
        currmax = max(currmax+n,n)
        currmin = min(currmin+n,n)

        total += n
        gmax = max(gmax,currmax)
        gmin = min(gmin,currmin)

    return max(gmax , total-gmin) if gmax>0 else max(nums)



nums = [5,-3,5]
#nums = [1,-2,3,-2]
nums = [-5,-5,-3]
print(max_sum(nums))
