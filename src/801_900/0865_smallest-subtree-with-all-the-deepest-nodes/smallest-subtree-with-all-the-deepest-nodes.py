# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        d = {None:-1}
        def dfs(root, parent):
            if not root:
                return
            d[root] = d[parent] + 1
            dfs(root.left, root)
            dfs(root.right, root)
        dfs(root, None)
        max_depth = max(d.itervalues())
        def dfs2(root):
            if not root or d.get(root, -1) == max_depth:
                return root
            left = dfs2(root.left)
            right = dfs2(root.right)
            if left and right:
                return root
            if left:
                return left
            if right:
                return right
            return None
        return dfs2(root)
            
            