class Solution(object):
	def minCostClimbingStairs(self, cost):
		"""
		:type cost: List[int]
		:rtype: int
		"""
		if not cost:
			return 0
		f1 = cost[0]
		f2 = cost[1]
		for i in xrange(2,len(cost)):
			tmp = min(f1,f2)
			f1 = f2
			f2 = tmp+cost[i]
		return min(f1,f2)
		
		
	# 递归+记忆化
	def minCostClimbingStairs(self, cost):
		"""
		:type cost: List[int]
		:rtype: int
		"""
		if not cost:
			return 0
		mem = dict()
		def f(index):
			if index==0 or index==1:
				return cost[index]
			if index in mem:
				return mem[index]
			if index==len(cost):
				mem[index] = min( f(index-1),f(index-2) )
			else:
				mem[index] = min( f(index-1), f(index-2) ) + cost[index]
			return mem[index]
		return f(len(cost))	