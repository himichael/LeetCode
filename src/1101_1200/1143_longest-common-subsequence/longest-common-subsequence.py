﻿class Solution(object):
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