# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        queue = []
        if root==None:
            return
        queue.append(root)
        while queue:
            size = len(queue)
            tmp = []
            for _ in range(size):
                element = queue.pop(0)
                tmp.append(element.val)
                if(element.left != None):
                    queue.append(element.left)
                if(element.right != None):
                    queue.append(element.right)
            res.append(tmp)
        return res
    