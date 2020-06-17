class Solution(object):
	def findSecondMinimumValue(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if not root:
			return -1
		s = set()
		def dfs(root):
			if not root:
				return
			s.add(root.val)
			dfs(root.left)
			dfs(root.right)
		dfs(root)
		if len(s)<2:
			return -1
		return sorted(list(s))[1]
		
		
		
	# 另一种解法	
	def findSecondMinimumValue(self, root):
		if not root:
			return 0
		first = root.val
		second = float("inf")
		def dfs(root):
			if not root:
				return float("inf")
			if root.val==first:
				return min( dfs(root.left),dfs(root.right) )
			return min( root.val,dfs(root.left),dfs(root.right) )
		second = dfs(root)
		if second==float("inf"):
			return -1
		return second

			
			