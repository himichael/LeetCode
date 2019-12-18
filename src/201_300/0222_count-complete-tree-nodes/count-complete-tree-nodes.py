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
		
		
		
	def countNodes(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if not root:
			return 0
		left_height,left = 0,root
		right_height,right = 0,root
		while left:
			left_height += 1
			left = left.left
		while right:
			right_height += 1
			right = right.right
		if left_height==right_height:
			return 2**left_height-1
		else:
			return self.countNodes(root.left)+self.countNodes(root.right)+1
        