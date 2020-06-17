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