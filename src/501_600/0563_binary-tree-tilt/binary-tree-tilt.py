# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def recursion(root):
            if(root==None):
                return 0
            left = recursion(root.left)
            right = recursion(root.right)
            self.res += abs(left - right)
            return root.val + left + right
        recursion(root)
        return self.res
        