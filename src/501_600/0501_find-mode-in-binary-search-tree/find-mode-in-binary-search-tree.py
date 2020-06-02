# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        if not root:
            return []
        d = dict()
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            val = root.val
            if val not in d:
                d[val] = [1,val]
            else:
                num = d[val][0]+1
                d[val] = [num,val]
            dfs(root.right)
        dfs(root)
        values = sorted(d.values(),key=lambda x:x[0])
        max_num = values[-1][0]
        ans = [values[-1][1]]
        for i in xrange(len(values)-2,-1,-1):
            if values[i][0]==max_num:
                ans.append(values[i][1])
        return ans


