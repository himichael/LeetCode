class Solution(object):
	def minPathSum(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""		
		if not grid:
			return 0
		n,m = len(grid),len(grid[0])
		if n==1:
			return sum(grid[0])
		for i in xrange(1,m):
			grid[0][i] = grid[0][i-1] + grid[0][i]
		for i in xrange(1,n):
			grid[i][0] = grid[i-1][0] + grid[i][0]
		for i in xrange(1,n):
			for j in xrange(1,m):
				tmp = grid[i][j]
				grid[i][j] = min(grid[i-1][j]+tmp,grid[i][j-1]+tmp)
		return grid[-1][-1]