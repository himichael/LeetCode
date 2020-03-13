class Solution(object):
	def dailyTemperatures(self, T):
		"""
		:type T: List[int]
		:rtype: List[int]
		"""
		if not T:
			return []
		n = len(T)
		res = [0 for _ in xrange(n)]
		stack = []
		for i in xrange(n):
			while stack and T[i]>T[stack[-1]]:
				res[stack[-1]] = i-stack[-1]
				stack.pop()
			stack.append(i)
		return res