class Solution(object):
	def containsDuplicate(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		if(not nums or len(nums)==0):
			return False
		s = set()
		for i in nums:
			if(i in s):
				return True
			s.add(i)
		return False