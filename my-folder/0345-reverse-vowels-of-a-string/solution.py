class Solution(object):
    def reverseVowels(self, s):
        vowels = ['a','e','i','o','u']
        left = 0
        right = len(s) - 1
        counter = 0
        chars = list(s)
        while (left <= right):
            while ( left < right and chars[left].lower() not in vowels):
                left += 1
            while (left < right and chars[right].lower()  not in vowels):
                right -= 1
            chars[left] , chars[right] = chars[right] , chars[left]
            left += 1
            right -= 1
        s = "".join(chars)
        return s


        
