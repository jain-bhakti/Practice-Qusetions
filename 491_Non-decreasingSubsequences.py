def BruteForce(nums):
    hash = dict()
    result = [[]]

    for i in range(len(nums)):
        l = list()
        for j in range(i,len(nums)):
            if nums[j] >= nums[i]:
                l.append(nums[j])

        if nums[i] not in hash:
            hash[nums[i]] = l

    #print(hash)

    def generateSublists(lst):
        # Base case
        if len(lst) == 0:
            return [[]]
    
        # Recursive case
        sublists = []
        first_element = lst[0]
        rest_list = lst[1:]
        sublists_of_rest = generateSublists(rest_list)
        # Generate sublists including first element
        for sublist in sublists_of_rest:
            sublists.append([first_element] + sublist)
        # Generate sublists excluding first element
        sublists.extend(sublists_of_rest)
    
        return sublists

    for value in hash.values():
        l = generateSublists(value)

        for i in l:
            if len(i)>=2 and i not in result:
                result.append(i)

    result.remove([])
    print(result)



def Efficient(nums):
    def helper(i,subseq):
        if i == n:
            if len(subseq) >= 2:
                res.add(tuple(subseq))

            return

        if not subseq or subseq[-1] <= nums[i]:
            helper(i+1,subseq+[nums[i]])

        helper(i+1,subseq)

    n = len(nums)
    res = set()
    helper(0,[])
    return res

nums = [4,4,3,2,1]
nums = [4,6,7,7]
BruteForce(nums)
print(list(Efficient(nums)))