class Solution(object):
	def longestCommonSubsequence(self, text1, text2):
		"""
		:type text1: str
		:type text2: str
		:rtype: int
		"""		
		n = len(text1)
		m = len(text2)
		dp = [ [0]*(m+1) for _ in xrange(n+1) ]
		for i in xrange(1,n+1):
			for j in xrange(1,m+1):
				if text1[i-1]==text2[j-1]:
					dp[i][j] = dp[i-1][j-1]+1
				else:
					dp[i][j] = max(dp[i-1][j], dp[i][j-1])
		return dp[-1][-1]
		
	# 递归+备忘录
	def longestCommonSubsequence(self, text1, text2):
		"""
		:type text1: str
		:type text2: str
		:rtype: int
		"""		
		n = len(text1)
		m = len(text2)
		mem = [ [-1]*(m) for _ in xrange(n) ]
		def dfs(i,j):
			if i==n or j==m:
				return 0
			if mem[i][j]>-1:
				return mem[i][j]
			if text1[i]==text2[j]:
				mem[i][j] = dfs(i+1,j+1)+1
				return mem[i][j]
				
			else:
				a = dfs(i,j+1)
				b = dfs(i+1,j)
				mem[i][j] = max(a,b)
				return mem[i][j]
		return dfs(0,0)