class Solution(object):
	def searchMatrix(self, matrix, target):
		"""
		:type matrix: List[List[int]]
		:type target: int
		:rtype: bool
		"""
		if not (matrix and matrix[0]):
			return False
		def binary_search(arr):
			begin,end = 0,len(arr)
			while begin<=end:
				mid = begin+(end-begin)/2
				if arr[mid]>target:
					end = mid-1
				elif arr[mid]<target:
					begin = mid+1
				else:
					return True
			return False
		
		begin,end = 0,len(matrix)-1
		arr_len = len(matrix[0])-1
		while begin<=end:
			mid = begin+(end-begin)/2
			if matrix[mid][0]<=target<=matrix[mid][arr_len]:
				return binary_search(matrix[mid])
			if matrix[mid][0]>target:
				end = mid-1
			elif matrix[mid][arr_len]<target:
				begin = mid+1
		return False