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
		
		
		
	# O(N)实现复杂度实现
	def insert(self, intervals, newInterval):
		if not (intervals or newInterval):
			return [newInterval] if newInterval else intervals
		new_start = newInterval[0]
		new_end = newInterval[1]
		n = len(intervals)
		index = 0
		output = []
		while index<n and intervals[index][0]<new_start:
			output.append(intervals[index])
			index += 1
		if not output or output[-1][-1]<new_start:
			output.append(newInterval)
		else:
			output[-1][-1] = max(output[-1][-1],new_end)
		while index<n:
			start,end = intervals[index]
			if output[-1][-1]<start:
				output.append(intervals[index])
			else:
				output[-1][-1] = max(output[-1][-1],end)
			index += 1
		return output
		
		