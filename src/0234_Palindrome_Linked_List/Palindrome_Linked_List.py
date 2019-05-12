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