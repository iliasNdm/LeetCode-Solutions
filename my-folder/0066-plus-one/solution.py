# class Solution(object):
#     def plusOne(self, digits):
#         n = len(digits)
#         multiplicator = 1
#         number = 0
#         for i in range(n-1,-1,-1):
#             number += digits[i] * multiplicator
#             multiplicator *= 10
        
#         number += 1
#         return [int(x) for x in str(number)]

class Solution(object):
    def plusOne(self, digits):
        n = len(digits)
        for i in range(n-1,-1,-1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            elif digits[i] == 9:
                digits[i] = 0
        return [1] + n*[0] 
        
