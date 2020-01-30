class Solution(object):
	def minEatingSpeed(self, piles, H):
		"""
		:type piles: List[int]
		:type H: int
		:rtype: int
		"""
		begin,end = 1,10**9
		def possible(k):
			return sum( (i-1)/k+1 for i in piles ) <= H
		while begin<end:
			mid = begin+(end-begin)/2
			if not possible(mid):
				begin = mid+1
			else:
				end = mid
		return begin