class Solution(object):
	def maxProduct(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if(len(nums)==0):
			return 0
		max_num = nums[0]
		min_num = nums[0]
		res = nums[0]
		for i in range(1,len(nums)):
			m = max(max_num*nums[i], min_num*nums[i], nums[i])
			n = min(max_num*nums[i], min_num*nums[i], nums[i])
			max_num,min_num = m,n
			res = max(max_num,res)
		return res