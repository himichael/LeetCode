class Solution(object):
    def createTargetArray(self, nums, index):
        res = []
        n = len(nums)
        for i in xrange(n):
            res.insert(index[i],nums[i])
        return res
    