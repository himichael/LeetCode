﻿class Solution(object):
	def isPowerOfFour(self, num):
		"""
		:type num: int
		:rtype: bool
		"""
		return (num>0) and ((num&(num-1)) == 0) and (bin(num)[2:].count("0")%2==0)