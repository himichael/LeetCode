class Solution(object):
	def maxDistance(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		if not grid:
			return 0
		dx = [0,1,0,-1]
		dy = [1,0,-1,0]
		queue = []
		N = len(grid)
		steps = -1
		for i in xrange(N):
			for j in xrange(N):
				if grid[i][j]==1:
					queue.append((i,j))
		if not queue or len(queue)==N**2:
			return -1
		while queue:
			size = len(queue)
			for _ in xrange(size):
				i,j = queue.pop(0)
				for k in xrange(4):
					x = i + dx[k]
					y = j + dy[k]
					if 0<=x<N and 0<=y<N and grid[x][y]==0:
						queue.append((x,y))
						grid[x][y] = -1
			steps += 1
		return steps