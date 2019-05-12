class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        res = nums[0]
        for i in range(len(nums)):
            if(sum>0):
                sum += nums[i]
            else:
                sum = nums[i]
            res = max(res,sum)
        return res