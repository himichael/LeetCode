﻿class Solution(object):
	def hasGroupsSizeX(self, deck):
		if not deck or len(deck)<2:
			return False
		N = len(deck)
		count = [0 for _ in xrange(10000)]
		for i in deck:
			count[i] += 1
		for x in xrange(2,N+1):
			if N%x==0:
				if all(v%x==0 for v in count):
					return True
		return False
		
		
		
	# 最大公约数实现	
	def hasGroupsSizeX(self, deck):
		if not deck or len(deck)<2:
			return False
		def gdc(a,b):
			return a if not b else gdc(b,a%b)
		N = len(deck)
		count = [0 for _ in xrange(10000)]
		res = -1
		for i in deck:
			count[i] += 1
		for i in xrange(10000):
			if count[i]>0:
				if res==-1:
					res = count[i]
				else:
					res = gdc(res,count[i])
		return res>=2
		

		
	# 用哈希表+GCD算法
	def hasGroupsSizeX(self, deck):
		"""
		:type deck: List[int]
		:rtype: bool
		"""
		if not deck or len(deck)<2:
			return False
		d = dict()
		for i in deck:
			d[i] = d.setdefault(i,0)+1
		def gcd(a,b):
			return a if not b else gcd(b,a%b)
		x = d[deck[0]]
		for k in d.values():
			if k==1:
				return False
			x = gcd(x,k)
		return x>=2
		
		