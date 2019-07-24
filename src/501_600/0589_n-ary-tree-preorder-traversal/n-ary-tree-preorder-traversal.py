"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        def recursion(root):
            if(root==None):
                return
            res.append(root.val)
            childrens = root.children
            for node in childrens:
                recursion(node)
        recursion(root)
        return res