class Solution(object):
	def arrangeCoins(self, n):
		"""
		:type n: int
		:rtype: int
		"""	
		if n ==0:
			return 0	
		k,i = n,1
		res = 0
		while i<=k:
			k -= i
			res = i
			i += 1
		return res