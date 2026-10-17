class Solution(object):
    def firstUniqChar(self, s):
        chars = list(s)
        unique_value = None
        counts = Counter(chars)
        for i in range (len(s)):
            if counts[s[i]] == 1:
                return i

        return -1
                

                

        
        
