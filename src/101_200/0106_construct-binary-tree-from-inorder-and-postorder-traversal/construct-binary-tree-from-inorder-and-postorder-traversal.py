# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def buildTree(self, inorder, postorder):
		"""
		:type inorder: List[int]
		:type postorder: List[int]
		:rtype: TreeNode
		"""
		def recursion(in_arr,post_arr):
			if(not in_arr or not post_arr):
				return None
			if(len(in_arr)==1 and len(post_arr)==1):
				return TreeNode(post_arr[-1])
			
			root = TreeNode(post_arr[-1])
			index = in_arr.index(post_arr[-1])
			in_left = in_arr[:index]
			in_right = in_arr[index+1:]
			
			post_left = post_arr[:len(in_left)]
			post_right = post_arr[len(in_left):-1]
			root.left = recursion(in_left,post_left)
			root.right = recursion(in_right,post_right)
			return root
		return recursion(inorder,postorder)
    
    