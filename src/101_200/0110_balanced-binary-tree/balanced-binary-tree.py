# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if(root == None):
            return True
        def depth(root):
            if(root == None):
                return 0
            return max( depth(root.left), depth(root.right) ) + 1
        return abs(depth(root.left)-depth(root.right))<2 and self.isBalanced(root.left) and self.isBalanced(root.right)
    