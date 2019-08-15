# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def rightSideView(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		if(root==None):
			return []
		res = []
		queue = []
		queue.append(root)
		while(queue):
			res.append(queue[-1].val)
			size = len(queue)
			for i in range(size):
				tmp = queue.pop(0)
				if(tmp.left != None):
					queue.append(tmp.left)
				if(tmp.right != None):
					queue.append(tmp.right)
		return res