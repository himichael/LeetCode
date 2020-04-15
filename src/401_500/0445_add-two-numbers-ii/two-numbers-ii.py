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
		
	
	
	# 基于栈的实现 
	def addTwoNumbers(self, l1, l2):	
		s1 = []
		s2 = []
		while l1:
			s1.append(l1.val)
			l1 = l1.next
		while l2:
			s2.append(l2.val)
			l2 = l2.next
		head = None
		carry = 0
		while s1 or s2:
			n = carry
			n += s1.pop() if s1 else 0
			n += s2.pop() if s2 else 0
			carry = 1 if n>=10 else 0
			cur = ListNode(n%10)
			cur.next = head
			head = cur
		if carry:
			cur = ListNode(1)
			cur.next = head
		return cur
		
		
		
	# 递归+反转
	def addTwoNumbers(self, l1, l2):	
		def reverse(head):
			pre,cur = None,head
			while cur:
				cur.next,pre,cur = pre,cur,cur.next
			return pre
		def add(a,b,carry):
			if not (a or b):
				return ListNode(1) if carry else None
			a = a if a else ListNode(0)
			b = b if b else ListNode(0)
			a.val = a.val+b.val+carry
			carry = 1 if a.val>=10 else 0
			a.val %= 10
			a.next = add(a.next,b.next,carry)
			return a 
		p = add( reverse(l1),reverse(l2),0 )
		return reverse(p)		
		
		
		
	#迭代+反转	
	def addTwoNumbers(self, l1, l2):		
		def reverse(head):
			pre,cur = None,head
			while cur:
				cur.next,pre,cur = pre,cur,cur.next
			return pre
		p = None
		l1 = reverse(l1)
		l2 = reverse(l2)
		a,b = l1,l2
		carry = 0
		while a or b:
			val = (a.val if a else 0) + (b.val if b else 0) + carry
			p = a if a else b
			carry = 1 if val>=10 else 0
			p.val = val%10
			a = a.next if a else None
			b = b.next if b else None
			p.next = a if a else b
		if carry:
			p.next = ListNode(1)
		return reverse(l1)		
		
		
		
		
		
		
		
		
		