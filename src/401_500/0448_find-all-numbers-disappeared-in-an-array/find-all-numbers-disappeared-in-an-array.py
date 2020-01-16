class Solution(object):
	def findDisappearedNumbers(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		s,res = set(),[]
		for i in nums:
			s.add(i)
		for i in xrange(1,len(nums)+1):
			if i not in s:
				res.append(i)
		return res