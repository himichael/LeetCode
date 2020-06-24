class Solution(object):
	def insert(self, intervals, newInterval):
		"""
		:type intervals: List[List[int]]
		:type newInterval: List[int]
		:rtype: List[List[int]]
		"""
		if not (intervals and newInterval):
			return [newInterval] if not intervals else intervals
		intervals.append(newInterval)
		intervals = sorted(intervals,key=lambda x:x[0])
		arr = [intervals[0]]
		n = len(intervals)
		for i in xrange(1,n):
			if arr[-1][-1]>=intervals[i][0]:
				arr[-1][-1] = max(arr[-1][-1],intervals[i][-1])
			else:
				arr.append(intervals[i])
		return arr