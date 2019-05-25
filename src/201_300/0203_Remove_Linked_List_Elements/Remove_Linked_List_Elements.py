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