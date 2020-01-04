class Solution(object):
	def searchMatrix(self, matrix, target):
		"""
		:type matrix: List[List[int]]
		:type target: int
		:rtype: bool
		"""
		if not matrix or not matrix[0]:
			return False
		heigh = len(matrix)
		width = len(matrix[0])
		# p = matrix[heigh-1][0]
		row,column = heigh-1,0
		while row>=0 and column<width:
			if matrix[row][column]>target:
				row -= 1
			elif matrix[row][column]<target:
				column += 1
			else:
				return True
		return False