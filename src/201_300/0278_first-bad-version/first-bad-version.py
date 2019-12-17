﻿# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
	def firstBadVersion(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n <=0:
			return x
		begin,end = 1,n
		while begin<=end:
			mid = begin+(end-begin)/2
			if isBadVersion(mid):
				end = mid-1
			else:
				begin = mid+1
		return begin