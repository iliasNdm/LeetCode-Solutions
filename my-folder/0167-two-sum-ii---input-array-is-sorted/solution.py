class Solution(object):
    def twoSum(self, numbers, target):
        n = len(numbers)
        left = 0
        right = n - 1
        somme = None
        while(somme!=target and left<right):
            somme = numbers[left] + numbers[right]
            if(somme>target):
                right -= 1
            if somme < target:
                left += 1
        return [left + 1,right +1]

        


