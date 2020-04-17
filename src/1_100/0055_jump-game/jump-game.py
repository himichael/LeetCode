class Solution(object):
	def canJump(self, nums):
		if not nums:
			return True
		max_jump = 0
		n = len(nums)
		for i in xrange(n):
			if max_jump>=i:
				max_jump = max(max_jump,i+nums[i])
		if max_jump>=n-1:
			return True
		return False