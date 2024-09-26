nums = [100,4,200,1,3,2]
nums.sort()                          #-1,-1,0,1,3,4,5,6,7,8,9
count = 1
temp = []

for i in range(len(nums)-1):
    if nums[i+1]-nums[i] == 1 or nums[i+1]-nums[i] == 0:
        if nums[i+1]-nums[i] == 0:
            count -= 1
        count += 1  
        temp.append(count)

    else:
        count = 1
        temp.append(count)
result = max(temp)
print(result)