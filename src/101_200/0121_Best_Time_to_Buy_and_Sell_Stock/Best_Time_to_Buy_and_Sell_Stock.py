class Solution(object):
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