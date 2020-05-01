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
		
		
		
	# 卡特兰数的一般项公式:  (2n)! / ((n+1)! * n!)
	def numTrees(self, n):
		if n<=0:
			return 0
		def f(i):
			return reduce(lambda x,y:x*y,range(1,i+1))
		return f(2*n)/(f(n+1)*f(n))