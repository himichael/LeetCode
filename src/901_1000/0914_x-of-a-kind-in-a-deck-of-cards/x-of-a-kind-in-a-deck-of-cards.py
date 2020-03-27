class Solution(object):
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