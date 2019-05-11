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
			tmp_max = max_num
			tmp_min = min_num
			if(nums[i] > 0):
				tmp_max = max(max_num*nums[i], nums[i])
				tmp_min = min(min_num*nums[i], nums[i])
			else:
				tmp_max = max(min_num*nums[i], nums[i])
				tmp_min = min(max_num*nums[i], nums[i])
			
			max_num = tmp_max
			min_num = tmp_min
			res = max(max_num,res)
		return res
