# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        def recursion(root,stack,value):
            if(root!=None and root.left==None and root.right==None):
                if(value+root.val == sum):
                    stack.append(root.val)
                    res.append(list(stack))
                    return
                if(value+root.val > sum):
                    return
            if(root==None):
                return
            recursion(root.left, stack+[root.val], value+root.val)
            recursion(root.right, stack+[root.val], value+root.val)
        recursion(root,[],0)
        return res    
		
		
	# 新的实现方式更高效	
	def pathSum(self, root, sum):
		"""
		:type root: TreeNode
		:type sum: int
		:rtype: List[List[int]]
		"""
		if(not root):
			return []
		res = []
		def dfs(root,arr,n):
			if root and (not root.left) and (not root.right):
				if(n+root.val == sum):
					tmp = arr+[root.val]
					res.append(list(tmp))
					return
			if root.left:
				dfs(root.left,arr+[root.val],n+root.val)
			if root.right:
				dfs(root.right,arr+[root.val],n+root.val)
		dfs(root,[],0)
		return res		