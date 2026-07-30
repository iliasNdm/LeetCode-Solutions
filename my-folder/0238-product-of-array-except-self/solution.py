class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        prefix = [1] * n 
        suffix = [1] * n 
        for i in range(1,n):
            prefix[i] = prefix[i - 1] * nums[i-1]
        for i in range(n-2,-1,-1):
            suffix[i] = nums[i+1] * suffix[i+1]
        return [a * b for a , b in zip(prefix,suffix)]

        


    
