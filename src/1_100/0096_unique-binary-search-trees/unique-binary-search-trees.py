class Solution(object):
	def numTrees(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n<=1:
			return 1
		res = [-1]*(n+1)
		res[0],res[1] = 1,1
		for i in xrange(2,n+1):
			res[i] = 0
			for j in xrange(0,i):
				res[i] += (res[j] * res[i-j-1])
		return res[-1]