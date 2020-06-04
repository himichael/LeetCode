# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
	def serialize(self, root):
		"""Encodes a tree to a single string.
		:type root: TreeNode
		:rtype: str
		"""
		if not root:
			return "#"
		def dfs(root,s):
			if not root:
				s += "#,"
			else:
				s += str(root.val)+","
				s = dfs(root.left,s)
				s = dfs(root.right,s)
			return s
		return dfs(root,"")

	def deserialize(self, data):
		"""Decodes your encoded data to tree.
		:type data: str
		:rtype: TreeNode
		"""
		def helper(s):
			if s[0]=="#":
				s.pop(0)
				return None
			root = TreeNode(s[0])
			s.pop(0)
			root.left = helper(s)
			root.right = helper(s)
			return root
		return helper(data.split(","))
			
			
			
		
		

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))