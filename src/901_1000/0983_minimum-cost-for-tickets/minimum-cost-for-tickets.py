class Solution(object):
	# 递归+记忆化
	def mincostTickets(self, days, costs):
		"""
		:type days: List[int]
		:type costs: List[int]
		:rtype: int
		"""
		days_set = set(days)
		mem = [-1 for _ in xrange(366)]
		def dfs(i):
			if i>365:
				return 0
			if mem[i]>-1:
				return mem[i]
			if i in days_set:
				mem[i] = min(dfs(i+1)+costs[0], dfs(i+7)+costs[1], dfs(i+30)+costs[2])
			else:
				mem[i] = dfs(i+1)
			return mem[i]
		return dfs(1)
		
		
		
	# 递归(超时)	
	def mincostTickets(self, days, costs):
		days_set = set(days)
		def dfs(i):
			if i>365:
				return 0
			if i in days_set:
				return min(dfs(i+1)+costs[0], dfs(i+7)+costs[1], dfs(i+30)+costs[2])
			else:
				return dfs(i+1)
		return dfs(1)
		
		
		
	# 动态规划
	def mincostTickets(self, days, costs):
		days_set = set(days)
		dp = [0]*366
		for i in xrange(1,days[-1]+1):
			if i in days_set:
				dp[i] = min(dp[i-1]+costs[0], dp[i-7]+costs[1], dp[i-30]+costs[2])
			else:
				dp[i] = dp[i-1]
		return dp[days[-1]]
		
		