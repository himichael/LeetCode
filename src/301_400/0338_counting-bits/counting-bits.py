﻿class Solution(object):
	def countBits(self, num):
		"""
		:type num: int
		:rtype: List[int]
		"""
		res = [0] * (num+1)
		for i in xrange(1,num+1):
			if( i%2==1 ):
				res[i] = res[i-1]+1
			else:
				res[i] = res[i/2]
		return res
		
		
		
	def countBits_2(self, num):
		"""
		:type num: int
		:rtype: List[int]
		"""
		res = [0]*(num+1)
		for i in xrange(1,num+1):
			res[i] += res[i&(i-1)] +1
		return res