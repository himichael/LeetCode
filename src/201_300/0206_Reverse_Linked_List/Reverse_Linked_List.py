# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur,pre = head,None
        while cur!=None:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
            #cur.next, pre, cur = pre, cur, cur.next
        return pre
		
	#递归解法	
    def reverseList_2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head==None and head.next==None):
            return head
        cur = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return cur		