# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if(head==None):
            return head
        dummy = ListNode(-1)
        i = dummy
        i.next = head
        j = head
        while(j != None):
            if(j.val == val):
                j = j.next
                continue
            i.next = j
            i = i.next
            j = j.next
        i.next = None
        return dummy.next
		
	# 更精简的实现
	def removeElements(self, head, val):
		"""
		:type head: ListNode
		:type val: int
		:rtype: ListNode
		"""
		p = ListNode(-1)
		p.next,h = head,p
		while p.next:
			if p.next.val==val:
				p.next = p.next.next
				continue
			p = p.next
		return h.next