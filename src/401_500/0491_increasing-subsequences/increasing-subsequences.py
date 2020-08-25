class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        tmp = []
        n = len(nums)
        def dfs(index,last):
            if index==n:
                if len(tmp)>=2:
                    res.append(list(tmp))
                return
            if nums[index]>=last:
                tmp.append(nums[index])
                dfs(index+1,nums[index])
                tmp.pop()
            if nums[index]!=last:
                dfs(index+1,last)
        dfs(0,float("-inf"))
        return res

