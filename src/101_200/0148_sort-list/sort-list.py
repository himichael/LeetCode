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
		
		
		
		
	# 精简代码	
    def sortList(self, head):
        self.p = ListNode(-1)
        def sort(node):
            if not (node and node.next):
                return node
            low,fast,self.p.next = self.p,self.p,node
            while fast and fast.next:
                low,fast = low.next,fast.next.next
            fast,low.next = low.next,None
            return merge(sort(self.p.next),sort(fast))
        
        def merge(a,b):
            if not (a and b):
                return a if a else b
            if a.val<=b.val:
                a.next = merge(a.next,b)
                return a
            else:
                b.next = merge(a,b.next)
                return b
        return sort(head)