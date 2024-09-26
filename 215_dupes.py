nums = [1,0,1,1]
k = 1
tada = {}

for i in range(len(nums)):
    if nums[i] not in tada:
        tada[nums[i]] = [i]

    else:
        tada[nums[i]].append(i)

for key,value in tada.items():
    if len(value) == 2:
        if abs(value[1]-value[0]) <= k :
            print(True)
    elif len(value) > 2:
        if abs(value[1]-value[0]) <= k or abs(value[2]-value[1]) <= k:
            print(True)
print(tada)