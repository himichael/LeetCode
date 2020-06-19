class Solution(object):
	def deepestLeavesSum(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if not root:
			return 0
		res = []
		def dfs(root,index):
			if not root:
				return
			if len(res)<index:
				res.append([])
			res[index-1].append(root.val)
			dfs(root.left,index+1)
			dfs(root.right,index+1)
		dfs(root,1)
		return sum(res[-1])