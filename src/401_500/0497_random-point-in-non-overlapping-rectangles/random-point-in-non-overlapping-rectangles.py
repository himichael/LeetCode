class Solution(object):

	def __init__(self, rects):
		"""
		:type rects: List[List[int]]
		"""
		self.rects = rects
		self.areas = []
		self.total = 0
		for arr in rects:
			self.total += (arr[2]-arr[0]+1)*(arr[3]-arr[1]+1)
			self.areas.append(self.total)

	def pick(self):
		"""
		:rtype: List[int]
		"""
		target = random.randint(0,self.total-1)
		begin,end = 0,len(self.areas)-1
		while begin<end:
			mid = begin+(end-begin)/2
			if self.areas[mid]<=target:
				begin = mid+1
			else:
				end = mid
		arr = self.rects[begin]
		width = arr[2]-arr[0]+1
		heigh = arr[3]-arr[1]+1
		base = self.areas[begin]- width*heigh
		return [ arr[0]+(target-base)%width, arr[1]+(target-base)/width ]
	


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()