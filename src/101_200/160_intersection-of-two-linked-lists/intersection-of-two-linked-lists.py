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
		
		
	# O(1)空间复杂度实现方式，当a遍历结束后从headB从新遍历，b遍历结束后从headA重新遍历
	# 直到找到a和b相等为止
	def getIntersectionNode(self, headA, headB):
		"""
		:type head1, head1: ListNode
		:rtype: ListNode
		"""
		a,b = headA,headB
		while a!=b:
			a = a.next if a else headB
			b = b.next if b else headA
		return a	