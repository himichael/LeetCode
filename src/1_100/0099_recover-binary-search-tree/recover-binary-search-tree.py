class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        res = []
        val = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            res.append(root)
            val.append(root.val)
            dfs(root.right)
            
        dfs(root)    
        index1 = -1
        index2 = -1
        for i in xrange(0,len(val)-1):
            if val[i]>val[i+1]:
                if index1==-1:
                    index1 = i
                    index2 = i+1
                else:
                    index2 = i+1
        if index1>-1 and index2>-1:
            tmp = res[index1].val
            res[index1].val = res[index2].val
            res[index2].val = tmp
			
			
			
	# O(h)空间复杂度的解法
    def recoverTree(self, root):
        self.index1 = None
        self.index2 = None
        self.pre = None
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if not self.pre:
                self.pre = root
            if self.pre.val<=root.val:
                self.pre = root 
            else:
                if not self.index1:
                    self.index1 = self.pre
                    self.index2 = root
                else:
                    self.index2 = root
            dfs(root.right)
        dfs(root)    
        tmp = self.index1.val
        self.index1.val = self.index2.val
        self.index2.val = tmp
		
		
		
	# 莫里斯遍历，遍历后恢复二叉树，真正的O(1)空间复杂度
    def recoverTree(self, root):
        x = None
        y = None
        morris_tmp = None
        pre = None    
        while root:
            if root.left:
                morris_tmp = root.left
                while morris_tmp.right and morris_tmp.right!=root:
                    morris_tmp = morris_tmp.right
                if morris_tmp.right is None:
                    morris_tmp.right = root
                    root = root.left
                else:
                    if pre and pre.val>root.val:
                        y = root
                        if not x:
                            x = pre
                    pre = root
                    morris_tmp.right = None
                    root = root.right
            else:
                if pre and pre.val>root.val:
                    y = root
                    if not x:
                        x = pre
                pre = root
                root = root.right
        if x and y:
            x.val,y.val = y.val,x.val	
		
		