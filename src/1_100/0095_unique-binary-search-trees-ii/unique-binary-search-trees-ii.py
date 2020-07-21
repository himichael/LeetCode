# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n<=0:
            return []
        def helper(begin,end):
            if begin>end:
                return [None]
            all_trees = []
            for i in xrange(begin,end+1):
                left_trees = helper(begin,i-1)
                right_trees = helper(i+1,end)
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        all_trees.append(root)
            return all_trees
        return helper(1,n)