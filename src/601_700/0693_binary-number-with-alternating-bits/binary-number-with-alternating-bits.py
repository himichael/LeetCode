class Solution(object):
	def hasAlternatingBits(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		mask = 1
		sign = n&1
		n = n>>1
		while( n>0 ):
			tmp = n&1
			if(tmp == sign):
				return False
			sign = tmp	
			n = n>>1
		return True