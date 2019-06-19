# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """ 
        if(preorder==None or len(preorder)==0):
            return []
        def recursive(root,i):
            if(root == None):
                return TreeNode(i)
            if(root.val > i):
                root.left = recursive(root.left, i)
            else:
                root.right = recursive(root.right, i)
            return root
        root = None
        for i in preorder:
            root = recursive(root, i)
        return root