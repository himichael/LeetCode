class Solution(object):
	def longestIncreasingPath(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: int
		"""	
		if not matrix:
			return 0
		n = len(matrix)
		m = len(matrix[0])
		#self.res = 0
		dx = [0,1,0,-1]
		dy = [1,0,-1,0]
		d = dict()
		def dfs(i,j,val):
			if (i,j) in d:
				return d[i,j]
			if 0>i or i>=n or 0>j or j>=m:
				d[i,j] = 0
				return 0
			incre = 0
			for k in xrange(4):
				x = i + dx[k]
				y = j + dy[k]
				if 0<=x<n and 0<=y<m and matrix[i][j]>matrix[x][y]:
					incre = max(incre,dfs(x,y,matrix[x][y]))
			d[i,j] = incre+1
			return incre+1
				
		res = 0	
		for i in xrange(n):
			for j in xrange(m):
				res = max( res,dfs(i,j,matrix[i][j]) )
		return res