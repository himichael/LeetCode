class Solution(object):
	def canPartition(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""				
		if not nums:
			return False
		total = sum(nums)
		if total%2==1:
			return False
		total /= 2
		n = len(nums)
		nums = sorted(nums,reverse=True)
		def dfs(index, remain):
			if remain==0:
				return True
			if index<n and remain<nums[index]:
				return False
			for i in xrange(index,n):
				if dfs(i+1, remain-nums[i]):
					return True
			return False
		return dfs(0,total)
		
	