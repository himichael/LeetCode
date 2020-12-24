class Solution(object):
    def candy(self, ratings):
        if not ratings:
            return 0
        n = len(ratings)
        dp = [0] * n
        left = 0
        right = 1
        res = 0
        for i in xrange(0, n):
            if i > 0 and ratings[i] > ratings[i - 1]:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = 1
        for i in xrange(n - 1, -1, -1):
            if i < n - 1 and ratings[i] > ratings[i + 1]:
                right += 1
            else:
                right = 1
            res += max(dp[i], right)
        return res