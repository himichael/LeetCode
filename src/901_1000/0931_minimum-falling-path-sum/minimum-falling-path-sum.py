class Solution(object):
    def minFallingPathSum(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0] * m for _ in range(n)]
        for j in range(m):
            dp[0][j] = matrix[0][j]
        for i in range(1, n):
            for j in range(m):
                dp[i][j] = dp[i - 1][j] + matrix[i][j]
                if j - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + matrix[i][j])
                if j + 1 < m:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j + 1] + matrix[i][j])
        return min(dp[-1])
        
        