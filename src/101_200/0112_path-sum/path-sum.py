# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        res = []
        def recursion(root,value,stack):
            if(root!=None and root.left==None and root.right==None):
                if(value+root.val == sum):
                    res.append(list(stack+[root.val]))
                    return
            if(root==None):
                return
            recursion(root.left,value+root.val,stack+[root.val])
            recursion(root.right,value+root.val,stack+[root.val])
        recursion(root,0,[])
        if(len(res) > 0):
            return True
        return False
		
	
	# 新的实现方式，更高效
	def hasPathSum(self, root, sum):
		"""
		:type root: TreeNode
		:type sum: int
		:rtype: bool
		"""
		if(not root):
			return False
		def recursion(root,n):
			if(not root.left and not root.right):
				if(n+root.val == sum):
					return True
				return False
			elif root.left and recursion(root.left, n+root.val):
				return True
			elif root.right and recursion(root.right, n+root.val):
				return True
			return False
		return recursion(root,0)