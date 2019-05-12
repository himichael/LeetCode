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