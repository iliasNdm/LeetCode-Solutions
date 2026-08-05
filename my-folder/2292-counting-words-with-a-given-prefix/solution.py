class Solution(object):
    def prefixCount(self, words, pref):
        counts = 0
        m = len(pref)
        for word in words:
            if word[0:m]== pref:
                counts += 1
        return counts


        
