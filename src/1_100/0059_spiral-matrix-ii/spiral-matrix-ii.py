class Solution(object):
	def generateMatrix(self, n):
		"""
		:type n: int
		:rtype: List[List[int]]
		"""	
		if n<=0:
			return []
		res = [[0 for _ in xrange(n)] for _ in xrange(n)]
		r1 = 0
		r2 = n-1
		c1 = 0
		c2 = n-1
		num = 1
		while r1<=r2 and c1<=c2:
			for c in xrange(c1,c2+1):
				res[r1][c] = num
				num += 1
			for r in xrange(r1+1,r2+1):
				res[r][c2] = num
				num += 1
			if r1<r2 and c1<c2:
				for c in xrange(c2-1,c1,-1):
					res[r2][c] = num
					num += 1
				for r in xrange(r2,r1,-1):
					res[r][c1] = num
					num += 1
			r1 += 1
			r2 -= 1
			c1 += 1
			c2 -= 1
		return res
		
		
	# 精简代码
	def generateMatrix(self, n):
		"""
		:type n: int
		:rtype: List[List[int]]
		"""	
		if n<=0:
			return []
		res = [[0 for _ in xrange(n)] for _ in xrange(n)]
		r1,c1 = 0,0
		r2,c2 = n-1,n-1
		num = 1
		while r1<=r2 and c1<=c2:
			for c in xrange(c1,c2+1):
				res[r1][c] = num
				num += 1
			for r in xrange(r1+1,r2):
				res[r][c2] = num
				num += 1
			for c in xrange(c2,c1,-1):
				res[r2][c] = num
				num += 1
			for r in xrange(r2,r1,-1):
				res[r][c1] = num
				num += 1
			r1, c1 = r1+1, c1+1
			r2, c2 = r2-1, c2-1
		return res
		
		