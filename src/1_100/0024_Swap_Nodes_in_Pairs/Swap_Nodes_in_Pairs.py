# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head==None or head.next==None):
            return head
        next_node = head.next
        head.next = self.swapPairs(next_node.next)
        next_node.next = head
        return next_node
		
		
	#不借助stack的实现方式	
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not (head and head.next):
            return head
        p = ListNode(-1)
        a,b,tmp,p.next = p,p,p,head
        while b and b.next and b.next.next:
            a,b = a.next,b.next.next
            tmp.next,a.next,b.next = b,b.next,a
            tmp,b = a,a
        return p.next
		
		
		
		

		