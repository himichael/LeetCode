class Solution(object):
	def maximalSquare(self, matrix):
		"""
		:type matrix: List[List[str]]
		:rtype: int
		"""
		if not matrix or not matrix[0]:
			return 0
		n = len(matrix)
		m = len(matrix[0])
		max_side = 0
		for i in xrange(n):
			for j in xrange(m):
				if matrix[i][j]=="1":
					max_side = max(max_side,1)
					current_max = min(n-i,m-j)
					for k in xrange(1,current_max):
						flag = True
						if matrix[i+k][j+k]=="0":
							break
						for v in xrange(k):
							if matrix[i+k][j+v]=="0" or matrix[i+v][j+k]=="0":
								flag = False
								break
						if flag:
							max_side = max(max_side,k+1)
						else:
							break
		return max_side**2