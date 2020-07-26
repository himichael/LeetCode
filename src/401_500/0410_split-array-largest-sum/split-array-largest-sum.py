class Solution(object):
	def splitArray(self, nums, m):
		"""
		:type nums: List[int]
		:type m: int
		:rtype: int
		"""
		if not nums:
			return 0
		total = sum(nums)
		n = len(nums)
		dp = [ [float("inf") for _ in xrange(m+1)] for _ in xrange(n+1) ]
		dp[0][0] = 0 
		sub = [0]
		for i in nums:
			sub.append(sub[-1]+i)
		for i in xrange(1,n+1):
			for j in xrange(1,min(i,m)+1):
				for k in xrange(i):
					dp[i][j] = min( dp[i][j], max(dp[k][j-1],sub[i]-sub[k]) )
		return dp[-1][-1]