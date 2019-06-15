"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if(root==None):
            return 0
        max_depth = 0
        for i in root.children:
            max_depth = max(max_depth, self.maxDepth(i))
        return max_depth + 1