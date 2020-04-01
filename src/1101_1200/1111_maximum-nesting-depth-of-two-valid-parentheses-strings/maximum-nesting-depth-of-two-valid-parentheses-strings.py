class Solution(object):
	def maxDepthAfterSplit(self, seq):
		"""
		:type seq: str
		:rtype: List[int]
		"""	
		if not seq:
			return []
		N = len(seq)
		ans = []
		idx = 1
		for c in seq:
			if c=="(":
				idx += 1
				ans.append(idx%2)
			else:
				ans.append(idx%2)
				idx -= 1
		return ans
		
		
		
	# 另一种实现	
	def maxDepthAfterSplit(self, seq):
		if not seq:
			return []
		N = len(seq)
		ans = [0 for i in xrange(N)]
		idx = 0
		for c in seq:
			if c=="(":
				ans[idx] = idx&1
			else:
				ans[idx] = (idx+1)&1
			idx += 1
		return ans	



		