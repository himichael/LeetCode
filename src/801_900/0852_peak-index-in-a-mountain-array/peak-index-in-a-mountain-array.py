class Solution(object):
	def peakIndexInMountainArray(self, A):
		"""
		:type A: List[int]
		:rtype: int
		"""		
		begin,end = 0,len(A)-1
		while begin<=end:
			mid = begin+(end-begin)/2
			left,right,n = A[mid-1],A[mid+1],A[mid]
			if left<n<right:
				begin = mid+1
			elif left>n>right:
				end = mid-1
			elif left<n>right:
				return mid