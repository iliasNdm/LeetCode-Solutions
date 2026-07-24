class Solution(object):
    def jump(self, nums):
        level = 0
        left = right = 0
        while (right < len(nums) - 1):
            farthest = 0
            for i in range(left , right + 1):
                farthest = max(farthest , i + nums[i])
            left = right + 1
            right = farthest
            level += 1
        return level 
