class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)
        def recursion(i,tmp):   
            res.append(tmp)
            for j in xrange(i,len(nums)):
                if(j>i and nums[j]==nums[j-1]):
                    continue
                recursion(j+1,tmp+[nums[j]])
        recursion(0,[])
        return res