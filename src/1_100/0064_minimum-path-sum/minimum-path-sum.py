class Solution(object):
	def minPathSum(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		if not grid:
			return 0
		m = len(grid)
		n = len(grid[0])
		for i in xrange(1,m):
			grid[i][0] += grid[i-1][0]
		for j in xrange(1,n):
			grid[0][j] += grid[0][j-1]
		for i in xrange(1,m):
			for j in xrange(1,n):
				grid[i][j] += min(grid[i-1][j], grid[i][j-1])
		return grid[-1][-1]
		
		
		
	# 递归(超时)	
	def minPathSum(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		if not (grid and grid[0]):
			return 0
		m = len(grid)
		n = len(grid[0])
		def dfs(i,j):
			if i==m or j==n:
				return float("inf")
			if i==m-1 and j==n-1:
				return grid[i][j]
			return grid[i][j] + min( dfs(i+1,j),dfs(i,j+1) ) 
		return dfs(0,0)