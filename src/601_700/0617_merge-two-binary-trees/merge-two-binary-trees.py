# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if(t1==None and t2==None):
            return None
        def recursive(root,r1,r2):
            if(r1==None and r2==None):
                return
            elif(r1==None):
                root = TreeNode(r2.val)
            elif(r2==None):
                root = TreeNode(r1.val)
            else:
                root = TreeNode(r1.val+r2.val)

            if(r1==None):
                root.left = recursive(root.left, None, r2.left)
            elif(r2==None):
                root.left = recursive(root.left, r1.left, None)
            else:
                root.left = recursive(root.left, r1.left, r2.left)
                
            if(r1==None):
                root.right = recursive(root.right, None, r2.right)
            elif(r2==None):
                root.right = recursive(root.right, r1.right, None)
            else:
                root.right = recursive(root.right, r1.right, r2.right)
            return root
        return recursive(None, t1, t2) 
    
    