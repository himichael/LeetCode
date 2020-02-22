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
        if not (head and head.next):
            return head
        p = ListNode(-1)
        low,fast,p.next = p,head,head
        while fast and fast.next:
            if low.next.val!=fast.next.val:
                low,fast = low.next,fast.next
            else:
                while fast.next and low.next.val==fast.next.val:
                    fast = fast.next
                fast,low.next = fast.next,fast.next
        return p.next
		
		
		
	def deleteDuplicates(self, head):
		p = ListNode(-1)
		a,b,p.next = p,head,head
		while b and b.next:
			if a.next.val!=b.next.val:
				a,b = a.next,b.next
			else:
				while b.next and a.next.val==b.next.val:
					b = b.next
				a.next,b = b.next,b.next
		return p.next
		
		