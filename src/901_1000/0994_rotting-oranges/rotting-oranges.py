class Solution(object):
	def orangesRotting(self, grid):
		if not grid:
			return -1
		n = len(grid)
		m = len(grid[0])
		rootList = []
		minutes = 0
		dx = [1,-1,0,0]
		dy = [0,0,1,-1]
		for i in xrange(n):
			for j in xrange(m):
				if grid[i][j]==2:
					rootList.append([i,j])
		while rootList:
			size = len(rootList)
			for _ in xrange(size):
				node = rootList.pop(0)
				x0 = node[0]
				y0 = node[1]
				for i in xrange(4):
					x = x0 + dx[i]
					y = y0 + dy[i]
					if 0<=x<n and 0<=y<m and grid[x][y]==1:
						grid[x][y] = 2
						rootList.append([x,y])
			if not rootList:
				break
			minutes += 1
		for i in xrange(n):
			for j in xrange(m):
				if grid[i][j]==1:
					return -1
		return minutes