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