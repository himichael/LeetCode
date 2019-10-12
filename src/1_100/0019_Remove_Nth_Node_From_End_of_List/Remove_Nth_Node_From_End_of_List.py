# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        s = []
        p = head
        while p:
            s.append(p.val)
            p = p.next
        count = len(s)
        if(n > count):
            return s
        del s[count-n]
        return s
        
    #用a，b两个指针方式实现
    def removeNthFromEnd_2(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p = ListNode(-1)
        p.next = head
        first = p
        second = p
        i = 0
        while(first.next!=None and i<n):
            first = first.next
            i += 1
        while(first.next != None):
            first = first.next
            second = second.next
        if(second.next != None):
            tmp = second.next
            second.next = tmp.next
            tmp = None
        return p.next
		
		
	# 精简代码
	def removeNthFromEnd(self, head, n):
		"""
		:type head: ListNode
		:type n: int
		:rtype: ListNode
		"""
		p = ListNode(-1)
		p.next,a,b = head,p,p
		while n>0 and b:
			b,n = b.next,n-1
		if not b:
			return head
		while b.next:
			a,b = a.next,b.next
		a.next = a.next.next
		return p.next	