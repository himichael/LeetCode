class Solution(object):
	def pathSum(self, root, sum):
		"""
		:type root: TreeNode
		:type sum: int
		:rtype: int
		"""		
		def paths(root,n):
			if not root:
				return 0
			res = 0
			if root.val==n:
				res += 1
			res += paths(root.left,n-root.val)
			res += paths(root.right,n-root.val)
			return res
			
		if not root:
			return 0
		r = paths(root,sum)
		left = self.pathSum(root.left,sum)
		right = self.pathSum(root.right,sum)
		return r+left+right