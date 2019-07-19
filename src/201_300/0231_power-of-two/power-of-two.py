class Solution(object):
	def isPowerOfTwo(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		if n==1:
			return True
		while(n > 1):
			n = n/2.0
		if n == 1.0 :
			return True
		else:
			return False