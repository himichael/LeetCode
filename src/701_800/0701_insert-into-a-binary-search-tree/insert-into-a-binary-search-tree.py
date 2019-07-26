# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def insertIntoBST(self, root, val):
		"""
		:type root: TreeNode
		:type val: int
		:rtype: TreeNode
		"""
		if(root==None):
			root = TreeNode(val)
			return root
		def recursion(node):
			if(node.val > val):
				if(node.left != None):
					recursion(node.left)
				else:
					node.left = TreeNode(val)
			else:
				if(node.right != None):
					recursion(node.right)
				else:
					node.right = TreeNode(val)
		recursion(root)
		return root