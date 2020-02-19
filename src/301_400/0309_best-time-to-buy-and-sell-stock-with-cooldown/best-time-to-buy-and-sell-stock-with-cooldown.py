class Solution(object):
	# 动态规划，二维数组
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""	
		if not prices:
			return 0
		n = len(prices)
		if n<=2:
			return 0 if n==1 else max(prices[1]-prices[0],0)
		dp = [[0 for _ in xrange(2)] for _ in xrange(n)]
		dp[0][0] = 0
		dp[0][1] = -prices[0]
		dp[1][0] = max(dp[0][0],dp[0][1]+prices[1])
		dp[1][1] = max(dp[0][1],-prices[1])
		for i in xrange(2,n):
			dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
			dp[i][1] = max(dp[i-1][1],dp[i-2][0]-prices[i])
		return max(dp[n-1][0],0)
	
	
	
	# 动态规划，二维数组+三种状态表示
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		if not prices:
			return 0
		n = len(prices)
		if n<2:
			return 0
		dp = [[0 for _ in xrange(3)] for _ in xrange(n)]
		dp[0][0] = 0
		dp[0][1] = -prices[0]
		dp[0][2] = 0
		for i in xrange(1,n):
			dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
			dp[i][1] = max(dp[i-1][1],dp[i-1][2]-prices[i])
			dp[i][2] = dp[i-1][0]
		return max(dp[n-1][0],dp[n-1][2],0)
		
		
		
		