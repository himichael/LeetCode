class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        number=0
        for i in range(len(nums)):
            number ^= nums[i]
        return number