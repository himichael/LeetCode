# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if(head==None or head.next==None):
            return 
        p = ListNode(-1)
        p.next = head
        first = p
        second = p
        
        #two point,find middle 
        while(second!=None and second.next!=None):
            first = first.next
            second = second.next.next
        pa = p.next
        pb = first.next
        first.next = None
        
        #reverse pb
        pre_b = None
        cur_b = pb
        while(cur_b != None):
            tmp = cur_b.next
            cur_b.next = pre_b
            pre_b = cur_b
            cur_b = tmp
        
        #merege two linklist,pa,pre_b
        pb = pre_b
        while(pa.next!=None and pb.next!=None):
            tmp_pa = pa.next
            tmp_pb = pb.next
            pa.next = pb
            pb.next = tmp_pa
            pa = tmp_pa
            pb = tmp_pb
        
        #processing boundary 
        if(pa.next!=None):
            tmp = pa.next
            pa.next = pb
            pb.next = tmp 
        else:
            pa.next = pb
