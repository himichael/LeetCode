class Solution(object):
	def runningSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		if not nums:
			return []
		n = len(nums)
		total = 0
		res = []
		for i in xrange(n):
			total += nums[i]
			res.append(total)
		return res