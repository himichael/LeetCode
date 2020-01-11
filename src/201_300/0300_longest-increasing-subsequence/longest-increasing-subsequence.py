class Solution(object):
	def lengthOfLIS(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums:
			return 0
		dp = [1 for i in xrange(len(nums))]
		res = 0
		for i in xrange(len(nums)):
			for j in xrange(0,i):
				if nums[i]>nums[j]:
					dp[i] = max(dp[i],dp[j]+1)
		
			res = max(res,dp[i])
		return res