class Solution(object):
	#动态规划一维数组
	def maxProfit(self, prices, fee):
		"""
		:type prices: List[int]
		:type fee: int
		:rtype: int
		"""
		if not prices:
			return 0
		n = len(prices)
		dp0 = 0
		dp1 = -prices[0]
		for i in xrange(1,n):
			dp0 = max(dp0,dp1+prices[i]-fee)
			dp1 = max(dp1,dp0-prices[i])
		return max(0,dp0,dp1)