class Solution(object):
	def spiralOrder(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""		
		if not matrix:
			return []
		res = []
		n = len(matrix)
		m = len(matrix[0])
		visited = [[False]*m for _ in xrange(n)]
		dr = [0,1,0,-1]
		dc = [1,0,-1,0]
		r, c, k = 0, 0, 0
		for _ in xrange(n*m):
			res.append(matrix[r][c])
			visited[r][c] = True
			i = r + dr[k]
			j = c + dc[k]
			if 0<=i<n and 0<=j<m and not visited[i][j]:
				r = i
				c = j
			else:
				k = (k+1)%4
				r = r + dr[k]
				c = c + dc[k]
		return res
		
		
		
	# 另一种解法
	def spiralOrder(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""		
		if not matrix:
			return []
		r1 = 0
		r2 = len(matrix)-1
		c1 = 0
		c2 = len(matrix[0])-1
		res = []
		while r1<=r2 and c1<=c2:
			for c in xrange(c1,c2+1):
				res.append(matrix[r1][c])
			for r in xrange(r1+1,r2+1):
				res.append(matrix[r][c2])
			if r1<r2 and c1<c2:
				for c in xrange(c2-1,c1,-1):
					res.append(matrix[r2][c])
				for r in xrange(r2,r1,-1):
					res.append(matrix[r][c1])
			r1 += 1
			r2 -= 1
			c1 += 1
			c2 -= 1
		return res
		
		
		