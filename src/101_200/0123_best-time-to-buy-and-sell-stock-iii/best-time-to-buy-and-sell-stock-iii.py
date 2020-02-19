class Solution(object):
	# 动态规划二位数组
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """        
        if not prices:
            return 0
        dp = [[[0 for _ in xrange(2)] for _ in xrange(3)] for _ in xrange(len(prices))]
        dp[0][0][0],dp[0][0][1] = 0,-prices[0]
        dp[0][1][0],dp[0][1][1] = float("-inf"),float("-inf")
        dp[0][2][0],dp[0][2][1] = float("-inf"),float("-inf")
        n = len(prices)
        for i in xrange(1,n):
            dp[i][0][0] = dp[i-1][0][0]
            dp[i][0][1] = max(dp[i-1][0][1], dp[i-1][0][0]-prices[i])
            dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][0][1]+prices[i])
            dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][1][0]-prices[i])
            dp[i][2][0] = max(dp[i-1][2][0], dp[i-1][1][1]+prices[i])
        return max(dp[n-1][0][0],dp[n-1][1][0],dp[n-1][2][0])
		
		
		
	# 动态规划状态压缩	
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """        
        if not prices:
            return 0
        s1 = -prices[0]
        s2 = float("-inf")
        s3 = float("-inf")
        s4 = float("-inf")
        for i in xrange(1,len(prices)):
            s1 = max(s1,-prices[i])
            s2 = max(s2,s1+prices[i])
            s3 = max(s3,s2-prices[i])
            s4 = max(s4,s3+prices[i])
        return max(s4,0)	



	# 递归+记忆化
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		if not prices:
			return 0
		k = 2
		n = len(prices)
		mem = [[[-1 for _ in xrange(2)] for _ in xrange(3)] for _ in xrange(n)]
		def dfs(index,count,status):
			if index==n or (count==k and status==0):
				return 0
			if mem[index][count][status]>-1:
				return mem[index][count][status]
			a = dfs(index+1,count,status)
			b,c = 0,0
			if status:
				b = dfs(index+1,count,0)+prices[index]
			else:
				c = dfs(index+1,count+1,1)-prices[index]
			mem[index][count][status] = max(a,b,c)
			return mem[index][count][status]
		return dfs(0,0,0)
		
	
	
	# 递归(超时)
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		if not prices:
			return 0
		k = 2
		n = len(prices)
		def dfs(index,count,status):
			if index==n or (count==k and status==0):
				return 0
			a = dfs(index+1,count,status)
			b,c = 0,0
			if status:
				b = dfs(index+1,count,0)+prices[index]
			else:
				c = dfs(index+1,count+1,1)-prices[index]
			return max(a,b,c)
		return dfs(0,0,0)
		
		
		
		
		
		
		
		
		