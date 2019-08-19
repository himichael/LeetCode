class Solution(object):
	def missingNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		nums = sorted(nums)
		i = 0
		while(i<len(nums)):
			if(i != nums[i]):
				return i
			i +=1
		return i