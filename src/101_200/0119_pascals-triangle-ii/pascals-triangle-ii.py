class Solution(object):
	def getRow(self, rowIndex):
		"""
		:type rowIndex: int
		:rtype: List[int]
		"""
		if rowIndex<2:
			return [1,1] if rowIndex==1 else [1]
		res = []
		pre = [1,1]
		for i in xrange(2,rowIndex+1):
			tmp = [1]*(i+1)
			for j in xrange(i+1):
				if j>0 and j<i:
					tmp[j] = pre[j-1]+pre[j]
			res,pre = tmp,tmp
		return res