class Solution(object):
    def minCut(self, s):
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = True
            for j in range(i + 1, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
        f = [float("inf")] * n
        for i in range(n):
            if dp[0][i]:
                f[i] = 0
            else:
                for j in range(i):
                    if dp[j + 1][i]:
                        f[i] = min(f[i], f[j] + 1)
        return f[-1]