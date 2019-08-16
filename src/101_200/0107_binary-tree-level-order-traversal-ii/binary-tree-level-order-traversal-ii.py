# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def levelOrderBottom(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		if(root==None):
			return []
		res = []
		queue = []
		queue.append(root)
		while(queue):
			size = len(queue)
			tmp = []
			for i in range(size):
				tmp.append(queue[i].val)
			res.append(tmp)
			for _ in range(size):
				tmp = queue.pop(0)
				if(tmp.left != None):
					queue.append(tmp.left)
				if(tmp.right != None):
					queue.append(tmp.right)
		res.reverse()
		return res
        