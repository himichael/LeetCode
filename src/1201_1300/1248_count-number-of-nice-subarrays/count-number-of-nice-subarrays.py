class Solution(object):
	def numberOfSubarrays(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: int
		"""
		if not nums or k<=0:
			return 0
		n = len(nums)
		dp = [0]*(n+1)
		dp[0] = 1
		ans = 0
		odd = 0
		for num in nums:
			if num%2==1:
				odd += 1
			if odd>=k:
				ans += dp[odd-k]
			dp[odd] += 1
		return ans