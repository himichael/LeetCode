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
		
    #前序遍历的非递归实现
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        while(len(stack)>0 or root!=None):
            if(root!=None):
                res.append(root.val)
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                root = node.right
        
        return res
        
        