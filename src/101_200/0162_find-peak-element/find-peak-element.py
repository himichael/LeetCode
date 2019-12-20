class Solution(object):
	def findPeakElement(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		begin,end = 0,len(nums)-1
		while begin<end:
			mid = begin+(end-begin)/2
			if nums[mid]>nums[mid+1]:
				end = mid
			else:
				begin = mid+1
	
		return begin