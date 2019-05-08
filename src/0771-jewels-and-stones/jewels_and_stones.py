class Solution(object):
	def numJewelsInStones(self, J, S):
		"""
		:type J: str
		:type S: str
		:rtype: int
		"""
		s = set()
		for i in range(len(J)):
			s.add(J[i])
		count = 0
		for i in range(len(S)):
			if(S[i] in s):
				count += 1
		return count