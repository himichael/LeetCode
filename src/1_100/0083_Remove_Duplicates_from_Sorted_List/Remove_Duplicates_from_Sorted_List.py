# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def deleteDuplicates(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		if not (head and head.nxt):
			return head
		i,j = head,head
		while j:
			if i.val!=j.val:
				i = i.next
				i.val = j.val
			j = j.next
		i.next = None
		return head