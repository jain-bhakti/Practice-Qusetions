#median of sorted arrays
def findMedianSortedArrays(nums1, nums2):
        nums1.extend(nums2)
        median = 0
        n = len(nums1)
        if n%2 == 0:
            median = (nums1[n//2]+nums1[(n//2)-1])/2
        else :
            median = nums1[n//2]
        return ('%.5f'%median)

nums1 =[1,2]
nums2 = [3]
print(findMedianSortedArrays(nums1,nums2))

#longest Palindrome substring
def Longestpalsubstr(s):
    
    n = len(s)

    start = 0
    maxlen = 1
    if n<2:
        print("single character")
    for i in range(n):
        high = i+1 
        low = i-1
        while(high<n and s[high] == s[i]):
            high+=1 
        
        while(low>=0 and s[low] == s[i]):
            low -=1 
        
        while(high<n and low>=0 and s[high]==s[low]):
            high+=1 
            low -=1 
        
        length = high-low-1
        if(maxlen<length):
            maxlen = length
            start = low+1 
        
    print(s[start:start+maxlen])

s = "abcnayan"
Longestpalsubstr(s)