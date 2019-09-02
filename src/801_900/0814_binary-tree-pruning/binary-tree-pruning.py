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
    
    