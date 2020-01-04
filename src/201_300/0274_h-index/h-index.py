class Solution(object):
	def hIndex(self, citations):
		"""
		:type citations: List[int]
		:rtype: int
		"""
		if not citations:
			return 0
		arr = sorted(citations)
		n = len(arr)
		self.res = 0
		def binary_search():
			begin,end = 0,n-1
			while begin<=end:
				mid = begin+(end-begin)/2
				h_index = n-mid
				if arr[mid]>=h_index:
					self.res = h_index
					end = mid-1
				else:
					begin = mid+1
		binary_search()
		return self.res