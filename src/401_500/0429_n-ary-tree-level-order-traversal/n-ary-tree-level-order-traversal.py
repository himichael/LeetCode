"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if(root==None):
            return []
        res = []
        queue = []
        queue.append(root)
        while(len(queue) > 0):
            size = len(queue)
            tmp = []
            for _ in range(size):
                node = queue.pop(0)
                tmp.append(node.val)
                childrens = node.children
                for c in childrens:
                    queue.append(c)
            res.append(tmp)       
        return res
    