class Solution(object):
	def findMaxConsecutiveOnes(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums:
			return 0
		left,right = 0,0
		res = 0
		while right<len(nums):
			if nums[right]==1:
				right += 1
				res = max(res,right-left)
			else:
				right = left = right+1
		return res