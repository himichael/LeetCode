class Solution(object):
	def rob(self, nums):
		if not nums:
			return 0
		n = len(nums)
		if n<=2:
			return max(nums)
		d = dict()
		def dfs(index,status,arr,d):
			if index==n-1:
				return 0
			if (index,status)in d:
				return d[index,status]
			a,b,c = 0,0,0
			a = dfs(index+1,status,arr,d)
			if status:
				b = dfs(index+1,0,arr,d)
			else:
				c = dfs(index+1,1,arr,d)+arr[index]
			d[index,status] = max(a,b,c)
			return d[index,status]
		return max(dfs(0,0,nums[0:n-1],dict()), dfs(0,0,nums[1:],dict()))