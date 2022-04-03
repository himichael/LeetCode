class Solution(object):
    def numSquares(self, n):
        if n <= 0:
            return 0
        dp = [0] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            tmp = 2 ** 31 - 1
            j = 1
            while j * j <= i:
                tmp = min(tmp, dp[i - j * j] + 1)
                j += 1
            dp[i] = tmp
        return dp[-1]