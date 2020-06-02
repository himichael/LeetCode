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
		def helper(root,s):
			if not root:
				s += "None,"
			else:
				s += str(root.val) + ","
				s = helper(root.left,s)
				s = helper(root.right,s)
			return s
		return helper(root,"")
		
        

	def deserialize(self, data):
		"""Decodes your encoded data to tree.
		:type data: str
		:rtype: TreeNode
		"""
		def helper(s):
			if s[0]=="None":
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