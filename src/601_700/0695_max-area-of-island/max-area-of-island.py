class Solution(object):
	def maxAreaOfIsland(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		if( not grid or len(grid[0])==0 ):
			return 0
		self.count = 0
		self.max_count = 0
		n = len(grid)
		m = len(grid[0])
		def recursion(i,j):
			if(0<=i<n and 0<=j<m and grid[i][j]==1):
				self.count += 1
				grid[i][j] = 0
				recursion(i,j+1)
				recursion(i,j-1)
				recursion(i-1,j)
				recursion(i+1,j)
		
		for i in xrange(n):
			for j in xrange(m):
				if( grid[i][j]==1 ):
					recursion(i,j)
					self.max_count = max(self.count,self.max_count)
					self.count = 0
		return self.max_count
		
		

	# 通过循环来迭代坐标，实现上下左右的DFS
	def maxAreaOfIsland_2(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		if( not grid or len(grid[0])==0 ):
			return 0
		self.count = 0
		self.max_count = 0
		n = len(grid)
		m = len(grid[0])
		dxy = ( (0,1),(0,-1),(1,0),(-1,0) )
		def recursion(i,j):
			if(0<=i<n and 0<=j<m and grid[i][j]==1):
				self.count += 1
				grid[i][j] = 0
				for d in dxy:
					recursion( i+d[0], j+d[1] )
					
		for i in xrange(n):
			for j in xrange(m):
				if( grid[i][j]==1 ):
					recursion(i,j)
					self.max_count = max(self.count,self.max_count)
					self.count = 0
		return self.max_count