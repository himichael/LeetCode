# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if( d<=0 ):
            return root
        if( d==1 ):
            node = TreeNode(v)
            node.left = root
            return node
        queue = []
        queue.append(root)
        for i in xrange(2,d):
            size = len(queue)
            for _ in xrange(size):
                node = queue.pop(0)
                if(node.left!=None):
                    queue.append(node.left)
                if(node.right!=None):
                    queue.append(node.right)
                   
        #for i in queue:
        #    print i.val
                  
        #linked node
        for i in xrange(len(queue)):
            node = queue[i]
            if(node.left==None and node.right==None):
                node.left = TreeNode(v)
                node.right = TreeNode(v)
                continue
            tmp1 = TreeNode(v)
            tmp1.left = node.left
            node.left = tmp1
            tmp2 = TreeNode(v)
            tmp2.right = node.right
            node.right = tmp2
        return root 
    
    
        