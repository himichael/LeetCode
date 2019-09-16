# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def flatten(self, root):
		"""
		:type root: TreeNode
		:rtype: None Do not return anything, modify root in-place instead.
		"""
		if(not root):
			return
		queue = []
		def recursion(root):
			if(not root):
				return
			queue.append(root)
			recursion(root.left)
			recursion(root.right)
		recursion(root)
		head = queue.pop(0)
		head.left = None
		head.right = None
		while queue:
			tmp = queue.pop(0)
			tmp.left = None
			tmp.right = None
			head.right = tmp
			head = tmp