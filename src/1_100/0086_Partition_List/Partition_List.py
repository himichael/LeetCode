# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        first,second = ListNode(-1),ListNode(-1)
        first.next,second.next,cur,a,b = head,head,head,first,second
        while cur:
            if cur.val<x:
                a.next,a,cur = cur,cur,cur.next
            else:
                b.next,b,cur = cur,cur,cur.next
        if a==first or b==second:
            return first.next if b==second else second.next
        a.next,b.next = second.next,None
        return first.next
        