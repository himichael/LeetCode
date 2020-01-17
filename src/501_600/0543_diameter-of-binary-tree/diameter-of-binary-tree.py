class Solution(object):
	def diameterOfBinaryTree(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		self.res = 0 
		def dfs(root):
			if not root or not (root.left or root.right):
				return 0
			left,right = 0,0
			if root.left:
				left = dfs(root.left)+1
			if root.right:
				right = dfs(root.right)+1
			self.res = max(self.res,left+right)
			return max(left,right)
		dfs(root)
		return self.res