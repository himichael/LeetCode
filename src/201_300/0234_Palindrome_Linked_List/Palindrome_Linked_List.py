# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None or head.next==None:
            return True
        
        s = []
        p = head
        while p:
            s.append(p.val)
            p = p.next
        a = s[:len(s)/2]
        b = s[len(s)/2:] if len(s)%2==0 else s[len(s)/2+1:]
        
        b.reverse()
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        return True
		
    def isPalindrome_2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if(head==None or head.next==None):
            return True
        p = ListNode(-1)
        p.next = head
        low = p
        fast = p
        while(fast!=None and fast.next!=None):
            low = low.next
            fast = fast.next.next
            
        second = low.next
        low.next = None 
        #reverse
        second_cur = second
        second_pre = None
        while(second_cur!=None):
            tmp = second_cur.next
            second_cur.next = second_pre
            second_pre = second_cur
            second_cur = tmp
        #comp second_pre head
        while(second_pre != None):
            if(second_pre.val != head.val):
                return False    
            second_pre = second_pre.next
            head = head.next
        return True		