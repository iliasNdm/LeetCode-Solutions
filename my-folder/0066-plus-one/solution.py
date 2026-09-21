class Solution(object):
    def plusOne(self, digits):
        n = len(digits)
        multiplicator = 1
        number = 0
        for i in range(n-1,-1,-1):
            number += digits[i] * multiplicator
            multiplicator *= 10
        
        number += 1
        return [int(x) for x in str(number)]
        
