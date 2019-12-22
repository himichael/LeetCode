class Solution(object):
	def findMin(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""	
		if not nums or len(nums)==1:
			return -1 if not nums else nums[0]
		begin,end = 0,len(nums)-1
		if nums[begin]< nums[end]:
			return nums[begin]
		while begin<=end:
			mid = begin+(end-begin)/2
			if nums[mid]>nums[mid+1]:
				return nums[mid+1]
			elif nums[mid]>=nums[0]:
				begin = mid+1
			else:
				end = mid-1
		return nums[begin]