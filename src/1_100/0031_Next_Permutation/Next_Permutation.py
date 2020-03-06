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
	

	
	# 重构代码
	def nextPermutation(self, nums):
		"""
		:type nums: List[int]
		:rtype: None Do not return anything, modify nums in-place instead.
		"""
		if not nums:
			return
		first = -1
		second = -1
		n = len(nums)
		for i in xrange(n-2,-1,-1):
			if nums[i]<nums[i+1]:
				first = i
				break
		if first>=0:
			for i in xrange(n-1,first,-1):
				if nums[i]>nums[first]:
					second = i
					break
		nums[first],nums[second] = nums[second],nums[first]
		self.reverse(nums,first+1,n-1)
	
	def reverse(self,nums,a,b):
		i,j = a,b
		while i<j:
			nums[i],nums[j] = nums[j],nums[i]
			i,j = i+1,j-1