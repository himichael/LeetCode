# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        arr = []
        while(head != None):
            arr.append(head.val)
            head = head.next
        def recursion(nums):
            if(nums==None or len(nums)==0):
                return None
            index = len(nums)/2
            root = TreeNode(nums[index])
            root.left = recursion(nums[:index])
            root.right = recursion(nums[index+1:])
            return root
        return recursion(arr)
        