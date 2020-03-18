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
		
		
		
	# 动态规划，精简代码
	def minPathSum(self, grid):	
		if not grid:
			return 0
		n = len(grid)
		m = len(grid[0])
		for i in xrange(1,m):
			grid[0][i] = grid[0][i-1] + grid[0][i]
		for i in xrange(1,n):
			grid[i][0] = grid[i-1][0] + grid[i][0]
		for i in xrange(1,n):
			for j in xrange(1,m):
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
		
		
		
	# 递归+记忆化
	def minPathSum(self, grid):
		if not grid:
			return 0
		n = len(grid)
		m = len(grid[0])
		mem = [[0 for _ in xrange(m)] for _ in xrange(n)]
		def dfs(i,j):
			if i==n or j==m:
				return float("inf")
			if i==n-1 and j==m-1:
				return grid[i][j]
			if mem[i][j]>0:
				return mem[i][j]
			grid[i][j] += min( dfs(i,j+1), dfs(i+1,j) )
			mem[i][j] = grid[i][j]
			return mem[i][j]
		return dfs(0,0)
		
		