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
		
		
	# 不借助stack的实现方式	
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = ListNode(-1)
        a,b,tmp,p.next = p,p,p,head
        while b and b.next and b.next.next:
            a,b,tmp.next = a.next,b.next.next,b.next.next
            a.next,b.next,tmp,b = b.next,a,a,a
        return p.next
		
		
	# 借助stack的方式，精简版
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        p,head,stack = head,dummy,[]
        while p and p.next:
            _,_,p = stack.append(p),stack.append(p.next),p.next.next
            dummy.next,dummy.next.next = stack.pop(),stack.pop()
            dummy,dummy.next = dummy.next.next,None
        if p:
            dummy.next = p
        return head.next
		
		
		
		

		