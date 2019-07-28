﻿# Definition for a binary tree node.
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
		
    def minDepth_2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(root == None):
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if(left==0 or right==0):
            return left+right+1
        return min(left,right)+1