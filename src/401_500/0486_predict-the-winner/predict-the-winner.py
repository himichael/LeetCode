class Solution(object):
    def PredictTheWinner(self, nums):
        n = len(nums)
        def dfs(i,j):
            if i==j:
                return nums[i]
            left = nums[i] - dfs(i+1,j)
            right = nums[j] - dfs(i,j-1)
            return max(left,right)
        return dfs(0,n-1)>=0
		


    def PredictTheWinner(self, nums):
        n = len(nums)
        dp = [[0 for _ in xrange(n)] for _ in xrange(n)]
        for i in xrange(n):
            dp[i][i] = nums[i]
        for i in xrange(n-2,-1,-1):
            for j in xrange(i+1,n):
                a = nums[i] - dp[i+1][j]
                b = nums[j] - dp[i][j-1]
                dp[i][j] = max(a,b)
        return dp[0][-1]>=0