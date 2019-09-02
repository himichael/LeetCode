# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
	def __init__(self, root):
		"""
		:type root: TreeNode
		"""
		self.root = root
		self.stack = []

	def next(self):
		"""
		@return the next smallest number
		:rtype: int
		"""
		res = -1
		while( self.root or self.stack ):
			if( self.root ):
				self.stack.append(self.root)
				self.root = self.root.left
			else:
				node = self.stack.pop()
				res = node.val
				self.root = node.right
				break
		return res
		

	def hasNext(self):
		"""
		@return whether we have a next smallest number
		:rtype: bool
		"""	
		if(self.root or self.stack):
			return True
		return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()