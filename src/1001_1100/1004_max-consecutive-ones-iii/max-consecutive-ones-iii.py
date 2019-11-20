class Solution(object):
	def longestOnes(self, A, K):
		"""
		:type A: List[int]
		:type K: int
		:rtype: int
		"""
		if not A:
			return 0
		left,right = 0,0
		windows = []
		n = K
		res = 0
		count = 0
		while right<len(A):
			c = A[right]
			if c==0:
				count += 1
			while count>K:
				if A[left]==0:
					count -= 1
				left += 1
			right += 1
			res = max(res,right-left)
		return res