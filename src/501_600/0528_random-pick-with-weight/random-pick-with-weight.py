class Solution(object):
	def __init__(self, w):
		"""
		:type w: List[int]
		"""
		self.total = 0
		self.res = []
		for i in w:
			self.total += i
			self.res.append(self.total)
		

	def pickIndex(self):
		"""
		:rtype: int
		"""
		target = random.randint(0,self.total-1)
		begin,end = 0,len(self.res)-1
		while begin<end:
			mid = begin+(end-begin)/2
			if self.res[mid]<=target:
				begin = mid+1
			else:
				end = mid
		return begin


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()