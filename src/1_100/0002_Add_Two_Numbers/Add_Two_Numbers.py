class Solution(object):
    def addTwoNumbers(self, l1, l2):
        a,b,p,carry = l1,l2,None,0
        while a or b:
            val = (a.val if a else 0)+(b.val if b else 0)+carry
            carry,val = val/10 if val>=10 else 0,val%10
            p,p.val = a if a else b,val
            a,b = a.next if a else None,b.next if b else None
            p.next = a if a else b
        if carry:
            p.next = ListNode(carry)
        return l1