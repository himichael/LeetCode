class Solution(object):
	def longestUnivaluePath(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""		
		if not root:
			return 0
		self.ans = 0
		def dfs(root):
			if not root:
				return 0
			left = dfs(root.left)
			right = dfs(root.right)
			if root.left and root.left.val==root.val:
				left += 1
			else:
				left = 0
			if root.right and root.right.val==root.val:
				right += 1
			else:
				right = 0
			self.ans = max(self.ans,left+right)
			return max(left,right)
		dfs(root)
		return self.ans