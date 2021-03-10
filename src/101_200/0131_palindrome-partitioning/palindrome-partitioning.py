class Solution(object):
    def partition(self, s):
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = True
            for j in range(i + 1, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
        res = []
        def dfs(i, arr):
            if i == n:
                res.append(arr[:])
                return
            for j in range(i, n):
                if dp[i][j]:
                    dfs(j + 1, arr + [s[i : j + 1]])
        dfs(0, [])
        return res