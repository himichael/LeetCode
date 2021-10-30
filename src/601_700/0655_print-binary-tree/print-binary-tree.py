# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        if not root:
            return []
        def getHigh(root):
            if not root:
                return 0
            return max(getHigh(root.left), getHigh(root.right)) + 1

        high = getHigh(root)
        ans = [["" for _ in range(2 ** high -1)] for _ in range(high)]
        def fill(root, i, left, right):
            if not root:
                return
            ans[i][(left + right) / 2] = str(root.val)
            fill(root.left, i + 1, left, (left + right) / 2)
            fill(root.right, i + 1, (left + right + 1) / 2, right)
        fill(root, 0, 0 , len(ans[0]))
        return ans



            


