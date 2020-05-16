class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        if not head:
            return 0
        arr = []
        while head:
            arr.append(str(head.val))
            head = head.next
        x = "".join(arr)
        return int(x,2)
		
		
		
	# 另一种实现，每次*2
    def getDecimalValue(self, head):
        if not head:
            return 0
        ans = 0
        while head:
            ans = ans*2 + head.val
            head = head.next
        return ans