#this is an O(1) space solution
class Solution(object):
     def reverse(self, nums, left, right):
        while left < right:
            nums[right] , nums[left] = nums[left] , nums[right]
            left += 1
            right -= 1

     def rotate(self, nums, k):
        n = len(nums)
        k = k%n
        self.reverse(nums,0,n-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,n-1)



# this is an O(n) solution

# class Solution(object):
#      def rotate(self, nums, k):
#         n = len(nums)
#         res = [0]*n
#         k = k % n
#         new_position = None
#         for i in range(n):
#             new_position = (i+k) % n
#             res[new_position] = nums[i]
#         nums[:] = res


