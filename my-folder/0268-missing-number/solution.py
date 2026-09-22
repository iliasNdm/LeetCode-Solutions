class Solution(object):
    def missingNumber(self, nums):
        numsSet = set(nums)
        for i in range(len(nums)+1):
            if i not in numsSet:
                return i
            
        
