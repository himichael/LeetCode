class Solution(object):
	def largestRectangleArea(self, heights):
		"""
		:type heights: List[int]
		:rtype: int
		"""
		if not heights:
			return 0
		heights = [0] + heights + [0]
		res = 0
		n = len(heights)
		stack = [0]
		for i in xrange(1,n):
			while heights[i]<heights[stack[-1]]:
				height = heights[stack.pop()]
				width = i-stack[-1]-1
				res = max(res,height*width)
			stack.append(i)
		return res