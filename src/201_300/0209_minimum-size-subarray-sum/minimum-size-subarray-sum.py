class Solution(object):
	def minSubArrayLen(self, s, nums):
		"""
		:type s: int
		:type nums: List[int]
		:rtype: int
		"""
		n = len(nums)
		left,total,res = 0,0,2**31-1
		for i in xrange(n):
			total += nums[i]
			while total >= s:
				res = min(res,i-left+1)
				total -= nums[left]
				left += 1
		return res if res!=(2**31-1) else 0