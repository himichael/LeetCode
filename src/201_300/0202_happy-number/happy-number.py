class Solution(object):
	def isHappy(self, n):
		"""
		:type n: int
		:rtype: bool
		"""		
		d = dict()
		def cacl_sum(i):
			num = 0
			while i>0:
				num = num + (i%10)*(i%10)
				i //= 10
			return num
		d[n] = 1
		while d[n]<2:
			if n==1:
				return True
			n = cacl_sum(n)
			d[n] = d.setdefault(n,0) + 1
		return False