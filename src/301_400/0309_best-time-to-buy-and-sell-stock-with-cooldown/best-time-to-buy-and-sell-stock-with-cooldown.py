class Solution(object):
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