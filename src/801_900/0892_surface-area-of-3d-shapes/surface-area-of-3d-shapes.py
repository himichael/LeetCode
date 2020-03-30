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
		
		
	# 做减法的思路，求出总表面，再减去未露出的面
	def surfaceArea(self, grid):
		if not grid:
			return 0
		N = len(grid)
		cubes = 0
		faces = 0
		for i in xrange(N):
			for j in xrange(N):
				cubes += grid[i][j]
				if grid[i][j]>0:
					faces += grid[i][j]-1
				if i>0:
					faces += min(grid[i-1][j],grid[i][j])
				if j>0:
					faces += min(grid[i][j-1],grid[i][j])
		return 6*cubes - 2*faces
		
		