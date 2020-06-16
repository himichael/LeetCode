class Solution(object):
	def minCameraCover(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if not root:
			return 0
		def dfs(root):
			if not root:
				return 0,0,float("inf")
			left = dfs(root.left)
			right = dfs(root.right)
			dp0 = left[1] + right[1]
			dp1 = min( left[2]+min(right[1],right[2]), right[2]+min(left[1],left[2]) )
			dp2 = min(left)+min(right)+1
			return dp0,dp1,dp2
		return min(dfs(root)[1:])