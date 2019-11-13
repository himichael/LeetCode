class Solution(object):
	def thirdMax(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		one,two,three = -2**63,-2**63,-2**63
		one = nums[0]
		for i in xrange(len(nums)):
			cur = nums[i]
			if one==cur or two==cur or three==cur:
				continue
			if one<cur:
				three,two,one = two,one,cur
			elif two<cur:
				three,two = two,cur
			elif three<cur:
				three = cur
		if three==(-2**63):
			return one
		return three