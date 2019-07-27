# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def recursion(root):
            if(root==None):
                return
            recursion(root.left)
            res.append(root.val)
            recursion(root.right)
        recursion(root)
        return res
		
    #非递归 实现
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res =  []
        while(len(stack)>0 or root!=None):
            if(root!=None):
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                res.append(node.val)
                root = node.right
        return res		