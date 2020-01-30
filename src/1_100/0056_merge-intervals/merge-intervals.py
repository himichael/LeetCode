class Solution(object):
	def merge(self, intervals):
		"""
		:type intervals: List[List[int]]
		:rtype: List[List[int]]
		"""		
		intervals.sort(key=lambda x:x[0])
		res = []
		for arr in intervals:
			if not res or res[-1][1]<arr[0]:
				res.append(arr)
			else:
				res[-1][1] = max(res[-1][1],arr[1])
		return res