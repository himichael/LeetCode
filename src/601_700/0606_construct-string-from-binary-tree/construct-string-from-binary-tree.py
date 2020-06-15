class Solution(object):
	def tree2str(self, t):
		"""
		:type t: TreeNode
		:rtype: str
		"""
		if not t:
			return ""
		res = []
		def dfs(root):
			if not root:
				return
			res.append(str(root.val))
			if root.left:
				res.append("(")
				dfs(root.left)
				res.append(")")
			if not root.left and root.right:
				res.append("()")
			if root.right:
				res.append("(")
				dfs(root.right)
				res.append(")")
		dfs(t)
		return "".join(res)