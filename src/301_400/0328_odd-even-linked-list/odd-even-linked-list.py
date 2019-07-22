# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def oddEvenList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		if(head==None):
			return head
		odd = ListNode(-1)
		event = ListNode(-1)
		a = head
		b = head.next
		odd.next = a
		event.next = b
		while(b!=None and b.next!=None):
			a.next = b.next
			b.next = a.next.next
			a = a.next
			b = b.next
		a.next = event.next
		return odd.next