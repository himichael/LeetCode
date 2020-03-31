class Solution(object):
	def sortArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		if not nums:
			return nums
		def partition(begin,end):
			povit = nums[end]
			j = begin
			for i in xrange(begin,end):
				if nums[i]<povit:
					nums[i],nums[j] = nums[j],nums[i]
					j += 1
			nums[j],nums[end] = nums[end],nums[j]
			return j
		def search(begin,end):
			if begin>=end:
				return
			pos = partition(begin,end)
			search(begin,pos-1)
			search(pos+1,end)
		search(0,len(nums)-1)
		return nums