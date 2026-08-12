class Solution(object):
    def longestConsecutive(self, nums):
        nums_set = set(nums)
        final_out = 0
        for x in nums_set:
            if x-1 not in nums_set:
                max_len = 1
                while x+1 in nums_set:
                    max_len += 1
                    x = x + 1

                if max_len >= final_out:
                    final_out = max_len
        return final_out
                 
        
        
