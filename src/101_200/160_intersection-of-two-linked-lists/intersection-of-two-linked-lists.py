# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	# 利用set实现
	def getIntersectionNode(self, headA, headB):
		"""
		:type head1, head1: ListNode
		:rtype: ListNode
		"""
		s,p,q = set(),headA,headB
		while p:
			_,p = s.add(p),p.next
		while q:
			if q in s:
				return q
			q = q.next
		return None
		
		
	