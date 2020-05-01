class Solution(object):
	def rotate(self, arr):
		for i in range(0,len(arr)/2):
			tmp = arr[i]
			arr[i] = arr[(len(arr)-1)-i]
			arr[(len(arr)-1)-i] = tmp
		for i in range(len(arr)):
			for j in range(i,len(arr)):
				tmp = arr[i][j]
				arr[i][j] = arr[j][i]
				arr[j][i] = tmp
				
				
				
	def rotate(self, matrix):
		matrix[:] = zip(*reversed(matrix))
		
		
		
	# 另一种原地解法
	def rotate(self, matrix):
		if not matrix:
			return []
		n = len(matrix)
		r = n//2-1
		c = (n-1)//2
		a = matrix
		for i in xrange(r+1):
			for j in xrange(c+1):
				a[i][j],a[j][n-i-1] = a[j][n-i-1],a[i][j]
				a[i][j],a[n-i-1][n-j-1] = a[n-i-1][n-j-1],a[i][j]
				a[i][j],a[n-j-1][i] = a[n-j-1][i],a[i][j]
				
				
				