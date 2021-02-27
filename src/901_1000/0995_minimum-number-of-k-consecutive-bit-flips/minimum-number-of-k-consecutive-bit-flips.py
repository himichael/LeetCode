class Solution(object):
    def minKBitFlips(self, A, K):
        n = len(A)
        dp = [0] * (n + 1)
        cnt = 0
        res = 0
        for i in xrange(n):
            cnt += dp[i]
            if (cnt + A[i]) % 2 == 0:
                if i + K > n:
                    return -1
                dp[i + K] -= 1
                cnt += 1
                res += 1
        return res