class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        return N%2==0
		
		
		
	# 动态规划
    def divisorGame(self, N):
        dp = [False for _ in xrange(N+3)]
        dp[1] = False
        dp[2] = True
        for i in xrange(3,N+1):
            for j in xrange(1,i):
                if i%j==0 and not dp[i-j]:
                    dp[i] = True
                    break
        return dp[N] 