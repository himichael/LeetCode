# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def mergeTwoLists(self, a1, a2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		if(a1==None):
			return a2
		if(a2==None):
			return a1
		head = ListNode(-1)
		p = head
		while(a1!=None and a2!=None):
			if(a1.val < a2.val):
				p.next = a1
				a1 = a1.next
			else:
				p.next = a2
				a2 = a2.next
			p = p.next
		if(a1!=None):
			p.next = a1
		else:
			p.next = a2
		return head.next
        