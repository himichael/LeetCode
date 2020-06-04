class Solution(object):
	def minDiffInBST(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		res =  []
		def dfs(root):
			if not root:
				return
			dfs(root.left)
			res.append(root.val)
			dfs(root.right)
		dfs(root)
		res = sorted(res)
		ans = float("inf")
		n = len(res)
		for i in xrange(1,n):
			if res[i]-res[i-1]<ans:
				ans = res[i]-res[i-1]
		return ans 