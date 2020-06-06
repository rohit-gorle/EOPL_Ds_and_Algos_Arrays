class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count_0 = 0
        count_1 = 0
        count_2 = 0
        for i in nums:
            if i == 0:
                count_0 += 1
            if i == 1:
                count_1 += 1
            if i == 2:
                count_2 += 1        
        
        nums[:count_0] = [0] * count_0
        nums[count_0:count_0+count_1] = [1] * count_1
        nums[count_0+count_1:] = [2] * count_2 
        
        print nums
     
