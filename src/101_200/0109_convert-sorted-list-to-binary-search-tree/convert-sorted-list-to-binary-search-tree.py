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


	# 链表双指针求中间节点，再不断递归构造二叉树
	def sortedListToBST(self, head):
		"""
		:type head: ListNode
		:rtype: TreeNode
		"""	
		if not head:
			return None
		self.p = ListNode(-1)
		def helper(node):
			if not (node and node.next):
				return TreeNode(node.val) if node else None
			a,b,self.p.next = self.p,node,node
			while b and b.next:
				a,b = a.next,b.next.next
			mid,a.next = a.next,None
			root = TreeNode(mid.val)
			root.left,root.right = helper(self.p.next),helper(mid.next)
			return root
		return helper(head)        