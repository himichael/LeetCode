# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if(root==None):
            return False
        if(root.left!=None and (root.left.val==x or root.left.val==y) ):
            return False
        if(root.right!=None and (root.right.val==x or root.right.val==y) ):
            return False
        self.x_depth = 0
        self.y_depth = 0
        def find_node(parent,num,depth,is_x):
            if(parent==None or (parent.left==None and parent.right==None)):
                return None
            if(parent.left!=None and parent.left.val==num):
                if(is_x):
                    self.x_depth = depth
                else:
                    self.y_depth = depth
                return parent
            if(parent.right!=None and parent.right.val==num):
                if(is_x):
                    self.x_depth = depth
                else:
                    self.y_depth = depth
                return parent
            node = find_node(parent.left,num,depth+1,is_x)
            if(node != None):
                return node
            return find_node(parent.right,num,depth+1,is_x)
        parent_x = find_node(root,x,0,True)
        parent_y = find_node(root,y,0,False)
        return (parent_x != parent_y) and (self.x_depth == self.y_depth)  
		
		
	# 用hash的方式实现
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if not root:
            return False
        depth = {}
        parent = {}
        def dfs(root,par):
            if root:
                if not par:
                    depth[root.val] = 0
                else:
                    depth[root.val] = depth[par.val]+1
                parent[root.val] = par
                if root.left:
                    dfs(root.left,root)
                if root.right:
                    dfs(root.right,root)
        dfs(root,None)
        print depth
        if depth[x]!=depth[y]:
            return False
        return parent[x]!=parent[y]
    
