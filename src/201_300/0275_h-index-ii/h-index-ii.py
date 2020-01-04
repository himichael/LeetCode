class Solution(object):
	def hIndex(self, citations):
		"""
		:type citations: List[int]
		:rtype: int
		"""
		if not citations:
			return 0
		begin,end = 0,len(citations)-1
		n,res = len(citations),0
		while begin<=end:
			mid = begin+(end-begin)/2
			h_index = n-mid
			if citations[mid]>=h_index:
				res = h_index
				end = mid-1
			else:
				begin = mid+1
		return res