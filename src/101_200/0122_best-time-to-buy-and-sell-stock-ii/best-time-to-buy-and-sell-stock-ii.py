class Solution(object):
	# 动态规划
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		if not prices:
			return 0
		n = len(prices)
		dp = [ [0]*2 for _ in xrange(n) ]
		dp[0][0] = 0
		dp[0][1] = -prices[0]
		res = 0
		for i in xrange(1,n):
			dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
			dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
		return dp[n-1][0]
	
	
	
	# O(1)空间复杂度的dp推导
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		if not prices:
			return 0
		n = len(prices)
		dp0 = 0
		dp1 = -prices[0]
		res = 0
		for i in xrange(1,n):
			dp0 = max(dp0,dp1+prices[i])
			dp1 = max(dp1,dp0-prices[i])
			res = max(res,dp0,dp1)
		return res
		
		
		
	# 递归，超时
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		if not prices:
			return 0
		n = len(prices)
		def dfs(index,status):
			if index==n:
				return 0
			if status:
				a = dfs(index+1,status)
				b = dfs(index+1,not status)+prices[index]
				return max(a,b)
			else:
				c = dfs(index+1,status)
				d = dfs(index+1,not status)-prices[index]
				return max(c,d)
		return dfs(0,0)
		
		
		
	# 优化上面的递归(超时)
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		if not prices:
			return 0
		n = len(prices)
		def dfs(index,status):
			if index==n:
				return 0
			a = dfs(index+1,status)
			b,c = 0,0
			if status:
				b = dfs(index+1,0)+prices[index]
			else:
				c = dfs(index+1,1)-prices[index]
			return max(a,b,c)
		return dfs(0,0)
		
		
	# 递归+记忆化
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		if not prices:
			return 0
		n = len(prices)
		mem = [ [-1]*2 for _ in xrange(n) ]
		def dfs(index,status):
			if index==n:
				return 0
			if mem[index][status]>-1:
				return mem[index][status]
			if status:
				a = dfs(index+1,status)
				b = dfs(index+1,not status)+prices[index]
				mem[index][status] = max(a,b)
			else:
				c = dfs(index+1,status)
				d = dfs(index+1,not status)-prices[index]
				mem[index][status] = max(c,d)
			return mem[index][status]
		return dfs(0,0)	
		
		