class Solution(object):
    def findTargetSumWays(self, nums, target):
        s = sum(nums)
        diff = s - target
        if diff < 0 or diff % 2 != 0:
            return 0
        n = len(nums)
        neg = diff // 2
        dp = [[0] * (neg + 1) for _ in range(n)]
        dp[0][0] = 1
        for i in range(n):
            dp[i][0] = 1
        for i in range(1, n):
            num = nums[i]
            for j in range(0, neg + 1):
                if j >= num:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - num]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]