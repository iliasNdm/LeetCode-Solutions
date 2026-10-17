class Solution(object):
    def reverseString(self, s):
        left = 0
        right = len(s) - 1
        counter  = 0
        while(left <= right):
            s[counter] , s[len(s) - (1+counter)] = s[len(s) - (1+counter)],s[counter]
            counter += 1
            left += 1
            right -= 1
        
        
        
