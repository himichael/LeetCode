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
		

	# 通过计数的方式遍历迭代链表	
	def oddEvenList(self, head):
		if not (head and head.next):
			return head
		headA,headB = ListNode(-1),ListNode(-1)
		a,b,i,p = headA,headB,1,head
		while p:
			if i%2==1:
				a.next,a = p,p
				p,a.next,i = p.next,None,i+1
			else:
				b.next,b = p,p
				p,b.next,i = p.next,None,i+1
		a.next = headB.next
		return headA.next
		
		
	# 精简代码实现
	def oddEvenList(self, head):
		if not (head and head.next):
			return head
		odd,event,a,b = head,head.next,head,head.next
		while b and b.next:
			a.next,b.next = b.next,b.next.next
			a,b = a.next,b.next
		a.next = event
		return odd	