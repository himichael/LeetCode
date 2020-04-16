class Solution(object):
	def updateMatrix(self, matrix):
		if not matrix:
			return []
		n = len(matrix)
		m = len(matrix[0])
		arr = [[0]*m for _ in xrange(n)]
		cache = set()
		queue = []
		for i in xrange(n):
			for j in xrange(m):
				if matrix[i][j]==0:
					queue.append((i,j))
					arr[i][j] = 0
					cache.add((i,j))
		while queue:
			i,j = queue.pop(0)
			for k in ((1,0),(0,1),(0,-1),(-1,0)):
				x = i + k[0]
				y = j + k[1]
				if 0<=x<n and 0<=y<m and (x,y) not in cache:
					arr[x][y] = arr[i][j]+1
					queue.append((x,y))
					cache.add((x,y))
		return arr
		
		
		
	# 增加dp实现	
	def updateMatrix(self, matrix):			
		if not matrix:
			return []
		n = len(matrix)
		m = len(matrix[0])
		dist = [[float("inf")]*m for _ in xrange(n)]
		for i in xrange(n):
			for j in xrange(m):
				if matrix[i][j]==0:
					dist[i][j] = 0
		for i in xrange(n):
			for j in xrange(m):
				if i-1>=0:
					dist[i][j] = min(dist[i][j],dist[i-1][j]+1)
				if j-1>=0:
					dist[i][j] = min(dist[i][j],dist[i][j-1]+1)
		for i in xrange(n-1,-1,-1):
			for j in xrange(m-1,-1,-1):
				if i+1<n:
					dist[i][j] = min(dist[i][j],dist[i+1][j]+1)
				if j+1<m:
					dist[i][j] = min(dist[i][j],dist[i][j+1]+1)
		return dist
		
		
		