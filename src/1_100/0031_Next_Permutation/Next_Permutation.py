class Solution(object):
	def nextPermutation(self, nums):
		"""
		:type nums: List[int]
		:rtype: None Do not return anything, modify nums in-place instead.
		"""
		if(nums==None or len(nums)==0 or len(nums)==1):
			return
			
		i = len(nums)-2
		while(i>=0 and nums[i+1]<=nums[i]):
			i -= 1
		if(i >= 0):
			j = len(nums)-1
			while(j>0 and nums[j]<=nums[i]):
				j -= 1
			nums[i],nums[j] = nums[j],nums[i]
		#reverse
		p = i+1
		q = len(nums)-1
		while(p < q):
			nums[p],nums[q] = nums[q],nums[p]
			p += 1
			q -= 1