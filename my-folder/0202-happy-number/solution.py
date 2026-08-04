class Solution(object):
    def sommeCarre(self,n):
        total = 0
        while(n>0):
            chifre = n % 10
            total += chifre * chifre
            n = n // 10
        return total
    def isHappy(self, n):
        seen = set()
        while(n != 1):
            n = self.sommeCarre(n)
            if n in seen :
                return False

            seen.add(n)
        return True
