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
		
		
		
		
	# 新的实现方式，只要遍历到根的左节点，右节点(子树) 放到 左节点(子树)的右边最后一位
    # 再将左节点(子树)挂到根节点的右边，最后设置根的左边为null
	def flatten_3(self, root):
		"""
		:type root: TreeNode
		:rtype: None Do not return anything, modify root in-place instead.
		"""
		if(not root):
			return None
		def helper(root):
			if(not root):
				return 
			helper(root.left)
			helper(root.right)
			if(root.left):
				pre = root.left
				while pre.right:
					pre = pre.right
				pre.right = root.right
				root.right = root.left
				root.left = None
		helper(root)		
		
		
		
	# 新的实现方式，这里借助stack，不断的遍历左右子树，然后先将右节点放入，再放入左节点
    # 下次栈pop()弹出的就是左节点，然后再不断迭代遍历左节点，再重复执行不断的层次遍历，借助pre节点，最后将整个树串起来	
    def flatten_4(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        stack = [root]
        pre = TreeNode(-1)
        while stack:
            node = stack.pop()
            pre.left = None
            pre.right = node
            if(node.right!=None):
                stack.append(node.right)
            if(node.left!=None):
                stack.append(node.left)
            pre = node		