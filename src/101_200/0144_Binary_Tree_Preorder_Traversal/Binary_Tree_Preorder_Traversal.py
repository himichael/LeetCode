# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def recursion(root):
            if(root == None):
                return
            res.append(root.val)
            recursion(root.left)
            recursion(root.right)
        recursion(root)
        return res
        
        