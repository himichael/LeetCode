﻿# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if(k==0 or head==None):
            return head
        p = head
        count = 0
        while(p != None):
            p = p.next
            count += 1
        k = k%count
        if(k == 0):
            return head
        i = 0
        p = ListNode(-1)
        p.next = head   
        while(i < count-k):
            p = p.next
            i += 1
        
        #假设链表是1->2->3->4->5 rotate是2，此时p为3，也就是新的tail
        #新的new_head就是4，也就是p.next
        #因为4后面还有元素，所以需要继续遍历到结束，然后将最后的元素->到原始的链表头(这里是head)
        new_tail = p
        new_head = p.next
        while(p.next != None):
            p = p.next
        p.next = head
        new_tail.next = None
        return new_head
        
		
		
	# 精简代码
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        p = ListNode(-1)
        cur,n,low,fast,p.next = head,0,p,p,head
        while cur:
            cur,n = cur.next,n+1
        if n==0 or k%n==0:
            return head
        n = k%n
        while fast.next and n>0:
            fast,n = fast.next,n-1
        while fast.next:
            low,fast = low.next,fast.next
        fast.next,p.next,low.next = head,low.next,None
        return p.next
		
		
		
	# 另一种解法，将链表变成环之后，再切断	
	def rotateRight(self, head, k):
		n,tail = 1,head
		while tail and tail.next:
			tail,n = tail.next,n+1
		k %= n
		if k==0 or n==0:
			return head
		tail.next = head
		for _ in xrange(n-k):
			tail = tail.next
		head,tail.next = tail.next,None
		return head	
		