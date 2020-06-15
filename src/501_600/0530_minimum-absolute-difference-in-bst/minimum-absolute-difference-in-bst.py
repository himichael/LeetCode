class Solution(object):
	def getMinimumDifference(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""	
		if not root:
			return 0
		self.pre = None
		self.diff = float("inf")
		def dfs(root):
			if not root:
				return
			dfs(root.left)
			if self.pre:
				t = abs(self.pre.val-root.val)
				if t<self.diff:
					self.diff = t
			self.pre = root
			dfs(root.right)
		dfs(root)
		return self.diff