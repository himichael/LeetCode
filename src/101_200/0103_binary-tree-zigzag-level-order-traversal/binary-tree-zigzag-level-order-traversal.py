# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if(root==None):
            return []
        queue = []
        res = []
        queue.append(root)
        is_reverse = False
        while(queue):
            size = len(queue)
            tmp = []
            for _ in range(size):
                node = queue.pop(0)
                if(node.left != None):
                    queue.append(node.left)
                if(node.right != None):
                    queue.append(node.right)
                tmp.append(node.val)
            if(is_reverse):
                tmp.reverse()
                res.append(tmp)
                is_reverse = False
            else:
                res.append(tmp)
                is_reverse = True
        return res
        