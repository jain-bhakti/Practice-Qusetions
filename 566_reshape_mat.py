mat = [[1,2],[3,4]]
r = 1
c = 4
nums = []
for i in mat:
    for j in i:
        nums.append(j)

if len(nums) < (r*c):
    print(mat)

else:
    results = []
        
    index = 0
    for i in range(r):
        results.append([])
        for j in range(c):
            results[i].append(nums[index])
            index += 1

        

print(results)



