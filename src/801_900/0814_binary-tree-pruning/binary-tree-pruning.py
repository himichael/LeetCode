# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if( not root ):
            return root    
        def recursion(root):
            if( not root ):
                return None
            if( root.val==1 and root.left==None and root.right==None ):
                return root
            if( root.val==0 and root.left==None and root.right==None):
                return None
            root.left = recursion(root.left)
            root.right = recursion(root.right)
            if( root.left==None and root.right==None and root.val==0 ):
                return None
            else:
                return root
        return recursion(root)
		
		
	# 新实现方式，代码更简洁	
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        def dfs(root):
            if not root:
                return None
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            if not root.left and not root.right and root.val==0:
                return None
            return root
        return dfs(root)
    		
    
    