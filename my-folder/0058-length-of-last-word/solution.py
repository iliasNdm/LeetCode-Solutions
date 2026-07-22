class Solution(object):
    def lengthOfLastWord(self, s):
        splited_string = s.split()
        return len(splited_string[-1])
