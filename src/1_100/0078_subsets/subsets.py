class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def recursive(i,tmp):
            res.append(tmp)
            for j in range(i,len(nums)):
                x = list(tmp)
                x.append(nums[j])
                recursive(j+1, x)
        recursive(0,[])
        return res