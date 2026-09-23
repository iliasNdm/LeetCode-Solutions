class Solution(object):
    def summaryRanges(self, nums):
        if nums == []:
            return []
        template = str(nums[0])
        result = []
        count = 0
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 1:
                count += 1
                continue
            elif count > 0:
                template += "->" + str(nums[i-1])
                result.append(template)
                count = 0
                template = str(nums[i])
            else :
                result.append(str(nums[i-1]))
                template = str(nums[i])
        
        if count > 0 :
           template += "->" + str(nums[-1])
        result.append(template)
        return result
                
                




            
