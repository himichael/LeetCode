# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not (s or t):
            return True
        if not (s and t):
            return False
        return self.isSameTree(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)

    def isSameTree(self,a,b):
        if not (a or b):
            return True
        if not (a and b):
            return False
        return a.val==b.val and self.isSameTree(a.left,b.left) and self.isSameTree(a.right,b.right)
		
		
		
		