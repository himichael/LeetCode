# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def countNodes(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		self.res = 0
		
		def recursion(root):
			if(root == None):
				return
			self.res += 1
			recursion(root.left)
			recursion(root.right)
		recursion(root)
		return self.res
        