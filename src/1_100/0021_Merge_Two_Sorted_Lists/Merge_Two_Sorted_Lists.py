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
        
		
	# or 实现方式，while循环判断a，b两个链表只要有一个不为空就继续遍历
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		if not (l1 and l2):
			return l2 if not l1 else l1
		p,head = ListNode(-1),l1 if l1.val<=l2.val else l2
		while l1 or l2:
			if not l1 or not l2:
				p.next = l1 if l1 else l2
				l1,l2,p = l1.next if l1 else None, l2.next if l2 else None, p.next
				continue
			elif l1.val<=l2.val:
				p.next,l1 = l1, l1.next
			else:
				p.next,l2 = l2, l2.next
			p = p.next
		return head
		
	
	# 更精简的实现方式
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		p = ListNode(-1)
		head = p
		while l1 and l2:
			if l1.val<=l2.val:
				p.next,l1 = l1,l1.next
			else:
				p.next,l2 = l2,l2.next
			p = p.next
		p.next = l1 if l1 else l2
		return head.next
	
	# 递归实现
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		if not (l1 and l2):
			return l1 if l1 else l2
		if l1.val<=l2.val:
			l1.next = self.mergeTwoLists(l1.next,l2)
			return l1
		else:
			l2.next = self.mergeTwoLists(l1,l2.next)
			return l2
	
	
	
	
	
	
	
	