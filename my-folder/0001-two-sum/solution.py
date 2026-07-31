class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement not in seen:
                seen[nums[i]] = i
            else :
                return [seen[complement],i]
                
        
