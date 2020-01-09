class Solution(object):
	def findClosestElements(self, arr, k, x):
		"""
		:type arr: List[int]
		:type k: int
		:type x: int
		:rtype: List[int]
		"""
		begin,end = 0,len(arr)-1
		i,j = 0,0
		while begin<=end:
			mid = begin+(end-begin)/2
			if arr[mid]>x:
				end = mid-1
			elif arr[mid]<x:
				begin = mid+1
			else:
				begin = mid
				break
		i,j = begin,begin+1
		if begin>end:
			i,j = end,begin
		while k>0:
			if i<0:
				j += 1
			elif j>=len(arr):
				i -= 1
			else:
				if abs(x-arr[i]) <= abs(x-arr[j]):
					i -= 1
				else:
					j += 1
			k -= 1
		return arr[i+1:j]