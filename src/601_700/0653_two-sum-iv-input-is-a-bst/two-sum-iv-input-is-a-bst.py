class Solution(object):
	def findTarget(self, root, k):
		"""
		:type root: TreeNode
		:type k: int
		:rtype: bool
		"""
		if not root:
			return False
		res = []
		def dfs(root):
			if not root:
				return
			res.append(root.val)
			dfs(root.left)
			dfs(root.right)
		dfs(root)
		s = set()
		for i in res:
			if k-i in s:
				return True
			s.add(i)
		return False