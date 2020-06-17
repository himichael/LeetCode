class Solution(object):
	def maxScoreSightseeingPair(self, A):
		"""
		:type A: List[int]
		:rtype: int
		"""
		if not A:
			return 0
		pre = A[0]+0
		n = len(A)
		res = 0
		for j in xrange(1,n):
			res = max(res,A[j]-j+pre)
			pre = max(pre,A[j]+j)
		return res