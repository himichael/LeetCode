class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+1)
        dp[0],dp[1] = 0,0
        res = 0
        for i in xrange(2,n+1):
            cur = 0
            for j in xrange(1,i):
                cur = max(cur, j*(i-j), j*dp[i-j])
            dp[i] = cur
            print dp
        return dp[-1]
        