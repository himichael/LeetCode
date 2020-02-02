class Solution(object):
	def uniquePathsWithObstacles(self, obstacleGrid):
		"""
		:type obstacleGrid: List[List[int]]
		:rtype: int
		"""
		if not obstacleGrid or obstacleGrid[0][0]==1:
			return 0
		m = len(obstacleGrid)
		n = len(obstacleGrid[0])
		dp = [ [0]*n for _ in xrange(m) ] 
		dp[0][0] = 1
		for i in xrange(1,m):
			if obstacleGrid[i][0]==0 and dp[i-1][0]==1:
				dp[i][0] = 1
			else:
				dp[i][0] = 0
		for j in xrange(1,n):
			if obstacleGrid[0][j]==0 and dp[0][j-1]==1:
				dp[0][j] = 1
			else:
				dp[0][j] = 0
		for i in xrange(1,m):
			for j in xrange(1,n):
				if obstacleGrid[i][j]==1:
					dp[i][j] = 0
				else:
					dp[i][j] = dp[i-1][j] + dp[i][j-1]
		return dp[-1][-1]