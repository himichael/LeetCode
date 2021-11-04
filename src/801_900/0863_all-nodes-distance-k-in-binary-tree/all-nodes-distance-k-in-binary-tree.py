# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        ans = []
        parents = {root.val : None}
        def findParents(root):
            if root.left:
                parents[root.left.val] = root
                findParents(root.left)
            if root.right:
                parents[root.right.val] = root
                findParents(root.right)
        def findAns(node, from_, depth):
            if not node:
                return
            if depth == k:
                ans.append(node.val)
                return
            if node.left != from_:
                findAns(node.left, node, depth + 1)
            if node.right != from_:
                findAns(node.right, node, depth + 1)
            if parents[node.val] != from_:
                findAns(parents[node.val], node, depth + 1)
        findParents(root)
        findAns(target, None, 0)
        return ans 