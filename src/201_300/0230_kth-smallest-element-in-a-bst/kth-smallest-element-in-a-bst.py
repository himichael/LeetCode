# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def kthSmallest(self, root, k):
		"""
		:type root: TreeNode
		:type k: int
		:rtype: int
		"""
		if( k<1):
			return None
		res = []
		def recursion(root):
			if(not root):
				return None
			recursion(root.left)
			res.append(root.val)
			recursion(root.right)
		recursion(root)
		if( k>len(res) ):
			return None
		return res[k-1]
    
	
	
	def kthSmallest_2(self, root, k):
		"""
		:type root: TreeNode
		:type k: int
		:rtype: int
		"""
		if( k<=0 ):
			return -1
		self.res = 0
		self.num = k
		def recursion(root):
			if(not root):
				return
			recursion(root.left)
			self.num -= 1
			if(self.num==0):
				#print root.val
				self.res = root.val
				return
			recursion(root.right)
		recursion(root)
		return self.res    
    
    