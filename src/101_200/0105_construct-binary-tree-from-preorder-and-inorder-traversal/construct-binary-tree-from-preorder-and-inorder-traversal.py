# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def recursion(pre_order, in_order):
            if(not pre_order or not in_order):
                return None        
            if( (pre_order and len(pre_order)==1) and (in_order and len(in_order)==1 )):
                return TreeNode(pre_order[0])
            root = TreeNode( pre_order[0] )
            #find root in in_order
            index = in_order.index(pre_order[0])
            in_left = in_order[0:index]
            in_right = in_order[index+1:]
            
            index = len(in_left)+1
            pre_left = pre_order[1:index]
            pre_right = pre_order[index:]
            
            root.left = recursion(pre_left, in_left)
            root.right = recursion(pre_right,in_right)
            return root
        return recursion(preorder,inorder)
		
		
		
	# 精简代码
	def buildTree(self, preorder, inorder):
		"""
		:type preorder: List[int]
		:type inorder: List[int]
		:rtype: TreeNode
		"""
		if not (preorder and inorder):
			return None
		root = TreeNode(preorder[0])
		mid_idx = inorder.index(preorder[0])
		root.left = self.buildTree(preorder[1:mid_idx+1],inorder[:mid_idx])
		root.right = self.buildTree(preorder[mid_idx+1:],inorder[mid_idx+1:])
		return root
		
        