# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxValue(self, root, k):
        def dfs(root, k):
            dp = [0] * (k + 1)
            if not root:
                return dp
            left = dfs(root.left, k)
            right = dfs(root.right, k)
            for i in range(k + 1):
                for j in range(k + 1):
                    dp[0] = max(dp[0], left[i] + right[j])
                    if i + j + 1 <= k:
                        dp[i + j + 1] = max(dp[i + j + 1], left[i] + right[j] + root.val)
            return dp
        return max(dfs(root,k))