class Solution(object):
    def trap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(nums==None or len(nums)==0):
            return 0
        left = 0
        right = len(nums)-1
        res = 0
        while(left < right):
            cur_min = min(nums[left],nums[right])
            if(cur_min == nums[left]):
                left += 1
                while(left<right and nums[left]<=cur_min):
                    res += cur_min - nums[left]
                    left += 1
            else:
                right -= 1
                while(left<right and nums[right]<=cur_min):
                    res += cur_min - nums[right]
                    right -= 1
        return res