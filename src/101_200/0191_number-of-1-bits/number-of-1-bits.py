class Solution(object):
	def hammingWeight(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		return bin(n).count("1")
		
		
		
	def hammingWeight_2(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		mask = 1
		res = 0
		for _ in xrange(32):
			if( n&mask ):
				res +=1
			mask = mask<<1
		return res		