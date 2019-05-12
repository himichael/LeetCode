class Solution(object):
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, a1, a2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if a1==None and a2==None:
            return []
        elif a1==None:
            return a2
        elif a2==None:
            return a1
        s=[]
        index=0
        while a1!=None and a2!=None:
            if a1.val <= a2.val:
                s.append(a1.val)
                a1=a1.next
            else:
                s.append(a2.val)
                a2=a2.next
        
        if a1!=None:
            while a1:
                s.append(a1.val)
                a1=a1.next
        if a2!=None:
            while a2:
                s.append(a2.val)
                a2=a2.next
        return s