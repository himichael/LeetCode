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
        
"""
        p=head
        count=0
        while p:
            p=p.next
            count+=1
            
        p=head
        num=count-n
        index=0
        if n > count:
            num=count

        while index<num:
            p=p.next
            index+=1
        print p.val
        if p.next==None:
            return
        if p.next.next!=None:
            tmp = p.next
            p.next=p.next.next
            tmp.next=None
"""