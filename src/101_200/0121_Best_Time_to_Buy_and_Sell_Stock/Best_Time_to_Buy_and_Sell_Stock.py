class Solution(object):
	# 贪心
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		if(prices==None or len(prices)==0):
			return 0
		min_v = prices[0]
		max_v = 0
		for i in range(len(prices)):
			min_v = min(min_v,prices[i])
			max_v = max(max_v,prices[i]-min_v)
		return max_v
		
		
		
	# 动态规划二维数组
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		if not prices:
			return 0
		n = len(prices)
		dp = [[0]*2 for _ in xrange(n)]
		dp[0][0] = 0
		dp[0][1] = -prices[0]
		res = 0
		for i in xrange(1,n):
			dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
			dp[i][1] = max(dp[i-1][1],-prices[i])
			res = max(res,dp[i][0],dp[i][1])
		return res
		
		
		
	# 动态规划O(1)	
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		if not prices:
			return 0
		dp0 = 0
		dp1 = -prices[0]
		n = len(prices)
		res = 0
		for i in xrange(1,n):
			dp0 = max(dp0,dp1+prices[i])
			dp1 = max(dp1,-prices[i])
			res = max(res,dp0,dp1)
		return res		
		
		
		
		
		
		
		
		
		
		