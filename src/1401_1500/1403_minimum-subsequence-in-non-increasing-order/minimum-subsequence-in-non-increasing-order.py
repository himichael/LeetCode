class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums)
        total = sum(nums)
        i = len(nums)-1
        save = 0
        res = []
        while i>=0 and save*2<=total:
            res.append(nums[i])
            save += nums[i]
            i -= 1
        return res
