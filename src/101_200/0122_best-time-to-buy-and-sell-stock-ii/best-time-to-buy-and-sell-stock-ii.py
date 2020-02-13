class Solution(object):
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
			res = max(res,dp[i][0],dp[i][1])
		return res
	
	
	
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
		self.res = 0
		n = len(prices)
		def dfs(index,profit,status):
			if index==n:
				self.res = max(self.res,profit)
				return
			if status:
				dfs(index+1,profit,status)
				dfs(index+1,profit+prices[index],0)
			else:
				dfs(index+1,profit,status)
				dfs(index+1,profit-prices[index],1)
		dfs(0,0,0)
		return self.res
		
		