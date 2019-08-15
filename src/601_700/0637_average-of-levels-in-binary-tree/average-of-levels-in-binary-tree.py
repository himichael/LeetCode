# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def averageOfLevels(self, root):
		"""
		:type root: TreeNode
		:rtype: List[float]
		"""
		if(root==None):
			return 0
		queue = []
		res = []
		queue.append(root)
		while(queue):
			tmp = 0.0
			size = len(queue)
			for i in range(size):
				tmp += queue[i].val
			tmp /= size
			res.append(tmp)
			for i in range(size):
				tmp = queue.pop(0)
				if(tmp.left != None):
					queue.append(tmp.left)
				if(tmp.right != None):
					queue.append(tmp.right)
		return res