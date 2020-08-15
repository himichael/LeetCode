class Solution(object):
	def removeBoxes(self, boxes):
		"""
		:type boxes: List[int]
		:rtype: int
		"""
		d = dict()
		def dfs(i,j,k):
			if (i,j,k) in d:
				return d[i,j,k]
			if i>j:
				d[i,j,k] = 0
				return 0
			while i<j and boxes[j]==boxes[j-1]:
				j -= 1
				k +=1
			tmp = dfs(i, j - 1, 0) + (k + 1) * (k + 1)
			value = tmp
			for index in xrange(i,j):
				if boxes[index]==boxes[j]:
					tmp = max(tmp,dfs(i,index,k+1) + dfs(index + 1, j - 1, 0))
			d[i,j,k] = tmp
			return d[i,j,k]
		return dfs(0,len(boxes)-1,0)