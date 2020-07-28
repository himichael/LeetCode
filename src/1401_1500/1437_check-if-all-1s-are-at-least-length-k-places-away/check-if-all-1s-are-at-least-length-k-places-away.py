class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        count = k
        for i in xrange(len(nums)):
            if nums[i]==1:
                if count<k:
                    return False
                count = 0
            else:
                count += 1
        return True    