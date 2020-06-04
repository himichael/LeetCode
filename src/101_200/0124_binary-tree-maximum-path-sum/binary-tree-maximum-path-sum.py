class Solution(object):
	def maxPathSum(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if not root:
			return 0
		self.ans = float("-inf")
		def dfs(root):
			if not root:
				return 0
			left = max(dfs(root.left),0)
			right = max(dfs(root.right),0)
			self.ans = max(root.val+left+right,self.ans)
			return root.val + max(left,right)
		dfs(root)
		return self.ans