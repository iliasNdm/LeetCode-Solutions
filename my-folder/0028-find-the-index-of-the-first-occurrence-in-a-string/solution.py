class Solution(object):
    def strStr(self, haystack, needle):
        h = len(haystack)
        n = len(needle)
        for i in range(h - n + 1):
            if needle == haystack[i : i + n ]:
                return i
            
        return -1
        
