<<<<<<< HEAD
﻿class Solution(object):
=======
class Solution(object):
>>>>>>> e5e30728299f8ba009756381d740382d8e330d12
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
<<<<<<< HEAD
        return l1
=======
        return l1
>>>>>>> e5e30728299f8ba009756381d740382d8e330d12
