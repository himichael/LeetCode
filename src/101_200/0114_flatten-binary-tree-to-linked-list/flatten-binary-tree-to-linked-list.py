# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def flatten(self, root):
		"""
		:type root: TreeNode
		:rtype: None Do not return anything, modify root in-place instead.
		"""
		if(not root):
			return
		queue = []
		def recursion(root):
			if(not root):
				return
			queue.append(root)
			recursion(root.left)
			recursion(root.right)
		recursion(root)
		head = queue.pop(0)
		head.left = None
		head.right = None
		while queue:
			tmp = queue.pop(0)
			tmp.left = None
			tmp.right = None
			head.right = tmp
			head = tmp
			
			
	# 另一种解法，前序遍历是:
    # 1.打印根节点 2.递归左边 3.递归后边
	# 也就是先根节点，再左右子树
    # 反序遍历是：
    # 1.递归右边 2.递归左边 3.打印根节点
	# 先右子树，再左子树，最后跟节点。这种解法用了一个pre节点，类似反转链表的方式，把整个二叉树的节点给串起来了
	def flatten_2(self, root):
		"""
		:type root: TreeNode
		:rtype: None Do not return anything, modify root in-place instead.
		"""
		if(not root):
			return
		self.pre = None
		def recursion(root):
			if(not root):
				return
			recursion(root.right)
			recursion(root.left)
			root.left = None
			root.right = self.pre
			self.pre = root
		recursion(root)
		
		
		