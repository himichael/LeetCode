# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check_left(value,root):
            if(root==None):
                return True
            if(root.val < value):
                if( check_left(value,root.left) ):
                    return check_left(value,root.right)
                else:
                    return False
            else:
                return False

        def check_right(value,root):
            if(root==None):
                return True
            if(root.val > value):
                if( check_right(value,root.left) ):
                    return check_right(value,root.right)
                else:
                    return False
            else:
                return False
        
        def recursion(root):
            if(root==None):
                return True
            if(root.left!=None):
                if(not check_left(root.val,root.left)):
                    return False
            if(root.right!=None):
                if(not check_right(root.val,root.right)):
                    return False
            res = recursion(root.left)
            if(res):
                return recursion(root.right)
            return res
        return recursion(root)
		
		
    def isValidBST_2(self, root):
        res = []
        def recursion(root):
            if(root==None):
                return
            recursion(root.left)
            res.append(root.val)
            recursion(root.right)
        recursion(root)
        return res == list(sorted(set(res)))


    def isValidBST_3(self, root):
        def recursion(root):
            if(root==None):
                return []
            return recursion(root.left) + [root.val] + recursion(root.right)
        res = recursion(root)
        return res == list(sorted(set(res)))















		
		
		
		