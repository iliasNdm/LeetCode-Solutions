class Solution(object):
    def moveZeroes(self, nums):
        insert_position = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_position] = nums[i]
                insert_position += 1
            
        for i in range(insert_position , len(nums)):
            nums[i] = 0
            

0 , 1 , 0 , 3 , 12
1 , 3, 12 , 
