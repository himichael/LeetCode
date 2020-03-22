class Solution(object):
	def minIncrementForUnique(self, A):
		"""
		:type A: List[int]
		:rtype: int
		"""
		if not A or len(A)<=1:
			return 0
		A = sorted(A)
		count = 0
		pre = A[0]
		for i in xrange(1,len(A)):
			if A[i]<=pre:
				increment = pre-A[i]+1
				count += increment
				pre = A[i] + increment
			else:
				pre = A[i]
		return count