class Solution:
    def reverse_2pointer(self,St): 
        #code here
        l,r = 0,len(St)-1
        while l<r:
            St[l],St[r] = St[r],St[l]
            l += 1
            r -= 1

    def reverse_recursion(self,St):
      pass

S1 = Solution()
St = [2,3,4,5,6]
S1.reverse_2pointer(St)
print(*St)
