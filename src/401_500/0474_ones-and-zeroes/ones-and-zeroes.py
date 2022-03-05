class Solution(object):
    def findMaxForm(self, strs, m, n):
        def zero_ones(s):
            res = [0,0]
            for i in s:
                res[ord(i) - ord('0')] += 1
            return res
        length = len(strs)
        dp = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(length + 1)]
        for i in range(1, len(strs) + 1):
            for j in range(0, m + 1):
                for k in range(0, n + 1):
                    zeros, ones = zero_ones(strs[i - 1])
                    if j >= zeros and k >= ones:
                        dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - zeros][k - ones] + 1)
                    else:
                        dp[i][j][k] = dp[i - 1][j][k]
        return dp[-1][-1][-1]    