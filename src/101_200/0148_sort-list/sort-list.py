# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def split_merge(p):
            if(p==None or p.next==None):
                return p
            h = ListNode(-1)
            h.next = p
            first = h
            second = h
            while(second!=None and second.next!=None):
                first = first.next
                second = second.next.next
            a = h.next
            b = first.next
            first.next = None
            split_a = split_merge(a)
            split_b = split_merge(b)
            return merge(split_a,split_b)
            
        
        def merge(pa,pb):
            if pa==None:
                return pb
            if pb==None:
                return pa
            if(pa.val < pb.val):
                pa.next = merge(pa.next,pb)
                return pa
            else:
                pb.next = merge(pa,pb.next)
                return pb
        
        return split_merge(head)