# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        def recursion(root,value):
            if(root!=None and root.left==None and root.right==None):
                res.append(value*10 + root.val)
                return
            if(root==None):
                return
            recursion(root.left, value*10+root.val)
            recursion(root.right, value*10+root.val)
        recursion(root,0)
        sum = 0
        for i in res:
            sum += i
        return sum