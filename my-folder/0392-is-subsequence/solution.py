class Solution(object):
    def isSubsequence(self, s, t):
        i = j = 0
        while j < len(t) and i < len(s):
            if t[j] == s[i]:
                i += 1
            j+=1
        return  i == len(s)
           


        
