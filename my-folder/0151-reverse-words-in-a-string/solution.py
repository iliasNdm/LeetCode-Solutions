class Solution(object):
    def reverseWords(self, s):
        splited_array = s.split()
        splited_array.reverse()
        return " ".join(splited_array)
        
