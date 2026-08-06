class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen = {}
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = i
            else :
                distance = abs(i - seen[nums[i]])
                if distance <= k:
                    return True
                else:
                    seen[nums[i]] = i
        return False

        
