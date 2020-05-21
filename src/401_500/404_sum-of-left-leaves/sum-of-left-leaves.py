# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        self.count = 0
        def dfs(root,is_left):
            if not root:
                return
            if root and not (root.left or root.right) and is_left:
                self.count += root.val
                return
            if root.left:
                dfs(root.left,True)
            if root.right:
                dfs(root.right,False)
        dfs(root.left,True)
        dfs(root.right,False)
        return self.count


