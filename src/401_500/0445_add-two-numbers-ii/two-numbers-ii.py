# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        s1 = []
        s2 = []
        while(p1!=None or p2!=None):
            if(p1 != None):
                s1.append(p1.val)
                p1 = p1.next
            if(p2 != None):
                s2.append(p2.val)
                p2 = p2.next
        
        res = s1
        res_len = len(s1)-1
        if(len(s1) < len(s2)):
            res = s2
            res_len = len(s2)-1
        i = len(s1)-1
        j = len(s2)-1
        is_carry = False
        while(i>=0 or j>=0):
            tmp_num = 0
            if(i >= 0):
                tmp_num += s1[i]
            if(j >= 0):
                tmp_num += s2[j]
            if(is_carry):
                tmp_num += 1
                if(tmp_num > 9):
                    tmp_num %= 10
                    is_carry = True
                else:
                    is_carry = False
            else:
                if(tmp_num > 9):
                    tmp_num %= 10
                    is_carry = True
                else:
                    is_carry = False
            res[res_len] = tmp_num
            i -= 1
            j -= 1
            res_len -=1
        
        res_link = l1
        if(len(s1) < len(s2)):
            res_link = l2
        head = ListNode(-1)
        head.next = res_link
        p = res_link
        i = 0
        while(p != None):
            p.val = res[i]
            p = p.next
            i += 1
        if(is_carry):
            carry_link = ListNode(1)
            head.next = carry_link
            carry_link.next = res_link
        return head.next