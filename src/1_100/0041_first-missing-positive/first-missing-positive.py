class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        s = set(nums)
        while i in s:
            i += 1
        return i
        