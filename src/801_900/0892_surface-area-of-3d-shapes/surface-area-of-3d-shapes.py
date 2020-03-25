class Solution(object):
	def uncommonFromSentences(self, A, B):
		"""
		:type A: str
		:type B: str
		:rtype: List[str]
		"""
		if not (A or B):
			return []
		d = dict()
		res = []
		for i in A.split(" "):
			if i not in d:
				d[i] = 1
			else:
				d[i] += 1
		for i in B.split(" "):
			if i not in d:
				d[i] = 1
			else:
				d[i] += 1
		for i in d:
			if d[i]==1:
				res.append(i)
		return res