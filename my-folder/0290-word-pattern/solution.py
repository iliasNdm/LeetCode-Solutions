class Solution(object):
    def wordPattern(self, pattern, s):
        mapPS , mapSP = {} , {}
        n = len(pattern)
        m = len(s.split())
        if (n != m):
            return False
        for c1 , word2 in zip(pattern , s.split()):
            if (c1 in mapPS and mapPS[c1] != word2) or (word2 in mapSP and mapSP[word2] != c1):
                return False
            mapPS[c1] = word2
            mapSP[word2] = c1

        return True
            
        
