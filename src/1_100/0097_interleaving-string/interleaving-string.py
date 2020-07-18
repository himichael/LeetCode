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