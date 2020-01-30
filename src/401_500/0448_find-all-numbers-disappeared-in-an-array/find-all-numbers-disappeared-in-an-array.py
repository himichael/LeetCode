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
		
		
	# O(n)时间复杂度解法
	def findDisappearedNumbers_2(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		res = []
		for i in xrange(len(nums)):
			new_index = abs(nums[i])-1
			if nums[new_index]>0:
				nums[new_index] *= -1
		for i in xrange(1,len(nums)+1):
			if nums[i-1]>0:
				res.append(i)
		return res