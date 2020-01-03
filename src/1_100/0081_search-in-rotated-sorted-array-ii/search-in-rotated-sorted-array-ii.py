class Solution(object):
	def search(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: bool
		"""
		if not nums:
			return False
		begin,end = 0,len(nums)-1
		while begin<=end:
			mid = begin+(end-begin)/2
			if nums[mid]==target:
				return True
			if nums[mid]>nums[begin]:
				if nums[begin]<=target<nums[mid]:
					end = mid-1
				else:
					begin = mid+1
			elif nums[mid]<nums[begin]:
				if nums[mid]<target<=nums[end]:
					begin = mid+1
				else:
					end = mid-1
			else:
				begin += 1
		return False