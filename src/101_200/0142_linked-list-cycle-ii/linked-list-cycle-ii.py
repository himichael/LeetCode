# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head == None):
            return None
        s = set()
        while(head != None):
            if(head in s):
                return head
            s.add(head)
            head = head.next
        return None
		
	#双指针解法	
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not (head and head.next):
            return None
        low,fast,p = head,head,head
        while fast and fast.next:
            low,fast = low.next,fast.next.next
            if low==fast:
                while low!=p:
                    low,p = low.next,p.next
                return p
        return None		