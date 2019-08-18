# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        res = []
        def recursion(root,value,stack):
            if(root!=None and root.left==None and root.right==None):
                if(value+root.val == sum):
                    res.append(list(stack+[root.val]))
                    return
            if(root==None):
                return
            recursion(root.left,value+root.val,stack+[root.val])
            recursion(root.right,value+root.val,stack+[root.val])
        recursion(root,0,[])
        if(len(res) > 0):
            return True
        return False