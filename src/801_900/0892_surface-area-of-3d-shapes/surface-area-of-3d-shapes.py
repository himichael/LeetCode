class Solution(object):
	def surfaceArea(self, grid):
		if not grid:
			return 0
		N = len(grid)
		res = 0
		for i in xrange(N):
			for j in xrange(N):
				if grid[i][j]>0:
					res += 2
					for r,c in ( (i+1,j),(i-1,j),(i,j+1),(i,j-1) ):
						if 0<=r<N and 0<=c<N:
							tmp = grid[r][c]
						else:
							tmp = 0
						res += max(grid[i][j]-tmp,0)
		return res