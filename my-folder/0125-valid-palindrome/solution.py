class Solution(object):
    def isPalindrome(self, s):
        n = len(s)
        l = 0
        r = n - 1
        
        while l < r :
            while l < r and not s[l].isalnum() :
                l+=1
            while l < r and not s[r].isalnum() :
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
            




        # complecite o(n)
        # s1  = re.sub(r'[^a-zA-Z0-9]', '', s)
        # s2 = s1.lower()
        # n = len(s2)
        # l = 0
        # r = n - 1
        # while(l< ):
        #     if s2[l] == s2[r]:
        #         l = l + 1
        #         r = r - 1
        #     else :
        #         return False
        # return True



        
