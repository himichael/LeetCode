class Solution(object):
    def balanceBST(self, root):
        arr = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)
        def helper(A):
            if not A:
                return
            mid = (0 + len(A)-1)//2
            root = TreeNode(A[mid])
            root.left = helper(A[:mid])
            root.right = helper(A[mid+1:])
            return root
        dfs(root)
        return helper(arr)