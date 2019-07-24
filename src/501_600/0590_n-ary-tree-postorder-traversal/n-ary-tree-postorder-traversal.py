"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        def recursion(root):
            if(root==None):
                return
            chilrens = root.children
            for node in chilrens:
                recursion(node) 
            res.append(root.val)
        recursion(root)
        return res
    
    