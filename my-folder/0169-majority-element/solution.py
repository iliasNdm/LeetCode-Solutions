from collections import Counter 

class Solution(object):
    def majorityElement(self, nums):
        condidate = None
        counts = 0
        for x in nums:
            if counts == 0:
                condidate = x
                counts = 1
            elif x == condidate:
                counts += 1
            else :
                counts -= 1
        return condidate


        
