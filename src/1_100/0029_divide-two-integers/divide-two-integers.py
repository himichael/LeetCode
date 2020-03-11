class Solution(object):		
	def divide(self, dividend, divisor):
		"""
		:type dividend: int
		:type divisor: int
		:rtype: int
		"""
		sign = (dividend>0) ^ (divisor>0)
		res = 0
		if divisor==1:
			return dividend
		if divisor==-1:
			if dividend==(-2**31):
				return 2**31-1
			return -dividend
		if dividend>0:
			dividend = -dividend
		if divisor>0:
			divisor = -divisor
		while dividend<=divisor:
			tmp_res = 1
			tmp = divisor
			while dividend<(tmp<<1):
				tmp = tmp<<1
				tmp_res = tmp_res<<1
			res += tmp_res
			dividend -= tmp
		if not sign:
			return res
		return -res