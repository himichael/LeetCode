# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if(root == None):
            return []
        res = []
        def recursion(root,stack):
            if(root==None):
                return
            if(root!=None and root.left==None and root.right==None):
                stack.append(root.val)
                res.append(list(stack))
                stack.pop()
                return
            recursion(root.left,stack+[root.val])
            recursion(root.right,stack+[root.val])
        recursion(root,[])
        result = []
        for i in range(len(res)):
            result.append( str(res[i])[1:-1].replace(" ","").replace(",","->") )
        return result