class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        result = len(nums) + 1
        somme = 0
        for right in range(len(nums)):
            somme += nums[right]
            while somme >= target :
                result = min(result , right - left + 1)
                somme -= nums[left]
                left += 1
                
       
            
            
        return 0 if result == len(nums) + 1 else result 

