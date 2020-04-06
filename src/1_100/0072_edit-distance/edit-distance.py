class Solution(object):
	def minDistance(self, word1, word2):
		"""
		:type word1: str
		:type word2: str
		:rtype: int
		"""		
		n = len(word1)
		m = len(word2)
		dp = [ [0]*(m+1) for _ in xrange(n+1) ]
		for i in xrange(1,m+1):
			dp[0][i] = dp[0][i-1]+1
		for i in xrange(1,n+1):
			dp[i][0] = dp[i-1][0]+1
		for i in xrange(1,n+1):
			for j in xrange(1,m+1):
				if word1[i-1]==word2[j-1]:
					dp[i][j] = dp[i-1][j-1]
				else:
					dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
		return dp[-1][-1]
		


	# 递归(超时)
	def minDistance(self, word1, word2):
		N = len(word1)
		M = len(word2)
		def dfs(i,j):
			if i==N or j==M:
				return N-i + M-j
			if word1[i]==word2[j]:
				return dfs(i+1,j+1)
			else:
				a = dfs(i+1,j)
				b = dfs(i,j+1)
				c = dfs(i+1,j+1)
				return min(a,b,c)+1
		return dfs(0,0)
		


	# 递归+备忘录模式	
	def minDistance(self, word1, word2):
		n = len(word1)
		m = len(word2)
		mem = [ [-1]*m for _ in xrange(n) ]
		def f(i,j):
			if i==n or j==m:
				return n-i + m-j
			if mem[i][j]>-1:
				return mem[i][j]
			if word1[i]==word2[j]:
				mem[i][j] = f(i+1,j+1)
				return mem[i][j]
			else:
				a = f(i,j+1)
				b = f(i+1,j)
				c = f(i+1,j+1)
				mem[i][j] = min(a,b,c)+1
				return mem[i][j]
		return f(0,0)


	# 动态规划，另一种初始化方式
	def minDistance(self, word1, word2):
		n = len(word1)
		m = len(word2)
		dp = [[-1 for _ in xrange(m+1)] for _ in xrange(n+1)]
		for i in xrange(n+1):
			dp[i][0] = i
		for j in xrange(m+1):
			dp[0][j] = j
		for i in xrange(1,n+1):
			for j in xrange(1,m+1):
				if word1[i-1]==word2[j-1]:
					dp[i][j] = dp[i-1][j-1]
				else:
					dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
		return dp[-1][-1]


