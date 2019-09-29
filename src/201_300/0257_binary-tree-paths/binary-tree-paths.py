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
		

	# 新的实现方式
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res = []
        def dfs(root,s):
            if not root:
                return
            if root and not root.left and not root.right:
                res.append(s+str(root.val))
                return
            dfs(root.left,s+str(root.val)+"->")
            dfs(root.right,s+str(root.val)+"->")
        dfs(root,"")    
        return res
        