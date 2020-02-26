class Solution(object):
	def threeSum(self, nums):
		if(len(nums) < 3):
			return []
		nums.sort()
		res = set()
		for i,v in enumerate(nums):
			d = {}
			for x in nums[i+1:]:
				if(x not in d):
					d[-v-x] = 1
				else:
					res.add((v,x,-v-x))
		return map(list,res)
		
		
		
	# 排序+双指针
	def threeSum(self, nums):
		if not nums:
			return []
		nums = sorted(nums)
		n = len(nums)
		res = []
		for k in xrange(n-2):
			if nums[k]>0:
				break
			if k>0 and nums[k-1]==nums[k]:
				continue
			i,j = k+1,n-1
			while i<j:
				tmp = nums[i]+nums[j]+nums[k]
				if tmp>0:
					j -= 1
				elif tmp<0:
					i += 1
				else:
					res.append([ nums[i],nums[j],nums[k] ])
					i += 1
					j -= 1
					while i<j and nums[i-1]==nums[i]:
						i += 1
					while i<j and nums[j+1]==nums[j]:
						j -= 1
		return res