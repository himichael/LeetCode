# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if(root==None or (root.left==None and root.right==None)):
            return True
        queue = []
        res = []
        queue.append(root)
        while(queue):
            size = len(queue)
            tmp = []
            for i in range(size):
                if(queue[i]==None):
                    tmp.append(None)
                else:
                    tmp.append(queue[i].val)
            res.append(tmp)
            for _ in range(size):
                tmp = queue.pop(0)
                if(tmp!=None):
                    if(tmp.left == None):
                        queue.append(None)
                    else:
                        queue.append(tmp.left)
                    if(tmp.right == None):
                        queue.append(None)
                    else:
                        queue.append(tmp.right)
        #print res
        for node in res:
            i = 0
            j = len(node)-1
            while(i <= j):
                if(node[i] != node[j]):
                    return False
                i += 1
                j -= 1
        return True
		
		
		
	# 用递归实现
	def isSymmetric_2(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		if(not root):
			return True
		def recursion(n1,n2):
			if(not n1 and not n2):
				return True
			if(not n1 and n2) or (n1 and not n2):
				return False
			if(n1.val != n2.val):
				return False
			if recursion(n1.left,n2.right):
				return recursion(n1.right,n2.left)
			return False
		return recursion(root.left,root.right)		