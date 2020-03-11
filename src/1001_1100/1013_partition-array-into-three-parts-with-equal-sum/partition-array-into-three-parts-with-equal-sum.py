class Solution(object):
	def canThreePartsEqualSum(self, A):
		if not A:
			return False
		total = 0
		for i in A:
			total += i
		if total%3!=0:
			return False
		s = 0
		count = 0
		for i in A:
			s += i
			if s==total/3:
				count += 1
				s = 0
		return count>=3