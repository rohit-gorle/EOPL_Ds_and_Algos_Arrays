class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        max_reach = 0
        for i in range(0,len(nums)):
            if(max_reach<i):
                return 0
            max_reach = max(max_reach,(i+nums[i]))
        return 1
