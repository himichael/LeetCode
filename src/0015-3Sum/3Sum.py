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