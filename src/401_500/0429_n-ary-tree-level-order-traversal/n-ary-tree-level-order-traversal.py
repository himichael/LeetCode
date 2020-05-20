"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if(root==None):
            return []
        res = []
        queue = []
        queue.append(root)
        while(len(queue) > 0):
            size = len(queue)
            tmp = []
            for _ in range(size):
                node = queue.pop(0)
                tmp.append(node.val)
                childrens = node.children
                for c in childrens:
                    queue.append(c)
            res.append(tmp)       
        return res
    
	
	
	# DFS实现
    def levelOrder(self, root):
        if not root:
            return []
        ans = []
        def dfs(root,index):
            if not root:
                return
            if len(ans)<=index-1:
                ans.append([])
            ans[index-1].append(root.val)
            for n in root.children:
                dfs(n,index+1)
        dfs(root,1)
        return ans	
		
		