class Solution:
    def maxCoins(self, nums):
        if not nums:
            return 0
        nums = [1] + nums + [1]
        n = len(nums)
        d = dict()
        def dfs(left,right):
            if (left,right) in d:
                return d[left,right]
            if left>=right-1:
                return 0
            res = 0
            for i in xrange(left+1,right):
                tmp = nums[left]*nums[i]*nums[right]
                tmp += dfs(left,i) + dfs(i,right)
                res = max(tmp,res)
            d[left,right] = res
            return res
        return dfs(0,n-1)