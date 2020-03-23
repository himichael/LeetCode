# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head==None or head.next==None):
            return head
        p = ListNode(-1)
        p.next = head
        first = p
        second = p
        while(second!=None and second.next!=None):
            first = first.next
            second = second.next.next
        if(second != None):
            return first.next
        return first
		
	# 精简代码
	def middleNode(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		if not (head and head.next):
			return head
		low,fast = head,head.next
		while fast and fast.next:
			low,fast = low.next,fast.next.next
		if fast:
			return low.next
		return low
		
		
		
	# 快慢指针都执行head	
	def middleNode(self, head):
		if not (head and head.next):
			return head
		a,b = head,head
		while b and b.next:
			a = a.next
			b = b.next.next
		return a 
		
		