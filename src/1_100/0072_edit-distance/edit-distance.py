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