class Solution(object):
	def orangesRotting(self, grid):
		if not grid:
			return 0
		dx = [1,-1,0,0]
		dy = [0,0,1,-1]
		rootList = []
		n = len(grid)
		m = len(grid[0])
		rootList = []
		minutes = 0
		for i in xrange(n):
			for j in xrange(m):
				if grid[i][j]==2:
					rootList.append([i,j])
		while rootList:
			size = len(rootList)
			tmp = []
			for node in rootList:
				x0 = node[0]
				y0 = node[1]
				for i in xrange(4):
					x = x0 + dx[i]
					y = y0 + dy[i]
					if 0<=x<n and 0<=y<m and grid[x][y]==1:
						grid[x][y] = 2
						tmp.append([x,y])
			if not tmp:
				break
			rootList = tmp
			minutes += 1
		# end while
		for i in xrange(n):
			for j in xrange(m):
				if grid[i][j]==1:
					return -1
		return minutes	