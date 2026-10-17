class Solution(object):
    def titleToNumber(self, columnTitle):
        multiplicator = 1
        result = 0
        for i in range(len(columnTitle)-1 , -1 , -1):
            result += (ord(columnTitle[i]) + 1 - ord('A')) * multiplicator
            multiplicator *= 26
        return result  
        







"ABCDEG"
