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
        
		
		
	# DFS实现
    def integerBreak(self, n):
        def dfs(n):
            if n<=2:
                return 1
            res = 0
            for i in xrange(1,n):
                res = max( res, i*(n-i), i*dfs(n-i) )
            return res
        return dfs(n)
		
		
		
	# DFS+记忆化	
    def integerBreak(self, n):
        d = dict()
        def dfs(n):
            if n in d:
                return d[n]
            if n<=2:
                d[2] = 1
                return 1
            res = 0
            for i in xrange(1,n):
                res = max( res, i*(n-i), i*dfs(n-i) )
            d[n] = res
            return res
        return dfs(n)
		
		