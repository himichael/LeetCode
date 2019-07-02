# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def minDepth(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if(root==None):
			return 0
		if(root.left==None and root.right==None):
			return 1
		res = 2**31-1
		if(root.left != None):
			res = min(self.minDepth(root.left),res)
		if(root.right != None):
			res = min(self.minDepth(root.right),res)
		return res+1