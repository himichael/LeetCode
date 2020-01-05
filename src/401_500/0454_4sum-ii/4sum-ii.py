class Solution(object):
	def fourSumCount(self, A, B, C, D):
		"""
		:type A: List[int]
		:type B: List[int]
		:type C: List[int]
		:type D: List[int]
		:rtype: int
		"""	
		d = dict()
		res = 0
		for i in A:
			for j in B:
				sum_ab = i+j
				d[sum_ab] = d.setdefault(sum_ab,0)+1
		for i in C:
			for j in D:
				tmp = 0-(i+j)
				if tmp in d:
					res += d[tmp]
		return res