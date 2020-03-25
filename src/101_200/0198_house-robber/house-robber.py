class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(nums==None or len(nums)==0):
            return 0
        #f(k) = max(f(k – 2) + A_kA k, f(k – 1))
        pre_max = 0
        cur_max = 0
        for i in nums:
            tmp = cur_max
            cur_max = max(pre_max+i,cur_max)
            pre_max = tmp
        return cur_max
		
		
		
	# 递归(超时)
	def rob(self, nums):
		if not nums:
			return 0
		n = len(nums)
		def dfs(index,status):
			if index==n:
				return 0
			a,b,c = 0,0,0
			a = dfs(index+1,status)
			if status==1:
				b = dfs(index+1,0)
			else:
				c = dfs(index+1,1)+nums[index]
			return max(a,b,c)
		return dfs(0,0)	
		
		
		
	# 递归+记忆化
	def rob(self, nums):
		if not nums:
			return 0
		n = len(nums)
		mem = [[-1 for _ in xrange(2)] for _ in xrange(n)]
		def dfs(index,status):
			if index==n:
				return 0
			if mem[index][status]>-1:
				return mem[index][status]
			a,b,c = 0,0,0
			a = dfs(index+1,status)
			if status==1:
				b = dfs(index+1,0)
			else:
				c = dfs(index+1,1)+nums[index]
			mem[index][status] = max(a,b,c)
			return mem[index][status]
		return dfs(0,0)	
		
		
		
	# 动态规划，一维数组
	def rob(self, nums):
		if not nums:
			return 0
		if len(nums)<2:
			return max(nums)
		n = len(nums)
		dp = [0 for _ in xrange(n)]
		dp[0] = nums[0]
		dp[1] = max(nums[0],nums[1])
		for i in xrange(2,n):
			dp[i] = max(dp[i-1],dp[i-2]+nums[i])
		return dp[-1]
		
		
		
	# 动态规划，O(1)空间
	def rob(self, nums):
		if not nums:
			return 0
		if len(nums)<2:
			return max(nums)
		n = len(nums)
		dp0 = nums[0]
		dp1 = max(nums[0],nums[1])
		for i in xrange(2,n):
			tmp = max(dp0+nums[i],dp1)
			dp0 = dp1
			dp1 = tmp
		return dp1
		
		
		
		
		
		