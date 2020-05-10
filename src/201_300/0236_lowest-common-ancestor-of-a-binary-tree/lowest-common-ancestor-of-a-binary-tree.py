# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_list = []
        q_list = []
        def find_node_p(root,value):
            if(root==None):
                return False
            if(root.val == value):
                return True
            p_list.append("left")
            if( find_node_p(root.left,value) ):
                return True
            p_list.pop()
            p_list.append("right")
            if( find_node_p(root.right,value) ):
                return True
            p_list.pop()
        
        def find_node_q(root,value):
            if(root==None):
                return False
            if(root.val == value):
                return True
            q_list.append("left")
            if( find_node_q(root.left,value) ):
                return True
            q_list.pop()
            q_list.append("right")
            if( find_node_q(root.right,value) ):
                return True
            q_list.pop()
            
        find_node_p(root,p.val)
        find_node_q(root,q.val)
        #print p_list
        #print q_list
        cur = root
        i = 0
        j = 0
        while(i<len(p_list) and j<len(q_list)):
            if(p_list[i]=="left" and q_list[j]=="left"):
                cur = cur.left
                i += 1
                j += 1
            elif(p_list[i]=="right" and q_list[j]=="right"):
                cur = cur.right
                i += 1
                j += 1
            else:
                break
        return cur
		
		
		
	# 增加新的实现方式，用字典保存节点->父节点的映射
	# 再不断迭代这个字典
	def lowestCommonAncestor(self, root, p, q):
		"""
		:type root: TreeNode
		:type p: TreeNode
		:type q: TreeNode
		:rtype: TreeNode
		"""
		d = {root:None}
		def dfs(root):
			if not root:
				return
			if root:
				if root.left:
					d[root.left] = root
				if root.right:
					d[root.right] = root
			dfs(root.left)
			dfs(root.right)
		dfs(root)
		a,b = p,q
		while a!=b:
			a = d.get(a,q)
			b = d.get(b,p)
		return a		
		
		
		
	# 不需要存储父节点方式的DFS解法
    def lowestCommonAncestor(self, root, p, q):
		def dfs(root,a,b):
			if not root or root==a or root==b:
				return root
			left = dfs(root.left,a,b)
			right = dfs(root.right,a,b)
			if left and right:
				return root
			else:
				return left if left else right
		return dfs(root,p,q)