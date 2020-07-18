class Solution(object):
	def isInterleave(self, s1, s2, s3):
		"""
		:type s1: str
		:type s2: str
		:type s3: str
		:rtype: bool
		"""
		s1_len = len(s1)
		s2_len = len(s2)
		n = len(s3)
		if s1_len+s2_len!=n:
			return False
		d = dict()
		def dfs(i,j,k):
			if (i,j,k) in d:
				return d[i,j,k]
			if i==s1_len and j==s2_len and k==n:
				return True
			if i>s1_len or j>s2_len or k>n:
				d[i,j,k] = False
				return False
			if i<s1_len and k<n and s1[i]==s3[k]:
				if dfs(i+1,j,k+1):
					d[i,j,k] = True
					return True
			if j<s2_len and k<n and s2[j]==s3[k]:
				if dfs(i,j+1,k+1):
					d[i,j,k] = True
					return True
			d[i,j,k] = False
			return False
		return dfs(0,0,0)
		
		
		
	# 动态规划，二维数组	
    def isInterleave(self, s1, s2, s3):
        s1_len = len(s1)
        s2_len = len(s2)
        s3_len = len(s3)
        if s1_len+s2_len != s3_len:
            return False
        dp = [[False for _ in xrange(s2_len+1)] for _ in xrange(s1_len+1)]
        dp[0][0] = True
        for i in xrange(1,s1_len+1):
            dp[i][0] = dp[i-1][0] and s1[i-1]==s3[i-1]
        for j in xrange(1,s2_len+1):
            dp[0][j] = dp[0][j-1] and s2[j-1]==s3[j-1]
        for i in xrange(1,s1_len+1):
            for j in xrange(1,s2_len+1):
                k = i+j-1
                dp[i][j] = (dp[i-1][j] and s1[i-1]==s3[k]) or (dp[i][j-1] and s2[j-1]==s3[k])
        return dp[-1][-1]
		
		