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