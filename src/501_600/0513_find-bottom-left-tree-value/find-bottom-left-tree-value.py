# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def findBottomLeftValue(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		res = []
		queue = []
		queue.append(root)
		while queue:
			size = len(queue)
			tmp = []
			for _ in xrange(size):
				node = queue.pop(0)
				tmp.append(node.val)
				if(node.left!=None):
					queue.append(node.left)
				if(node.right!=None):
					queue.append(node.right)
			res.append(tmp)
		return res[-1][0]