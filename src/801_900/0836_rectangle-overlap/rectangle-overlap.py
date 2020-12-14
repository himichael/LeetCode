class Solution(object):
	def isRectangleOverlap(self, rec1, rec2):
		"""
		:type rec1: List[int]
		:type rec2: List[int]
		:rtype: bool
		"""
		x = not (rec1[2]<=rec2[0] or rec2[2]<=rec1[0])
		y = not (rec1[3]<=rec2[1] or rec2[3]<=rec1[1])
		return x and y
		
		
		
	# 题目增加了一些测试用例，原解法不能通过，新的实现可以通过	
    def isRectangleOverlap(self, rec1, rec2):
        if rec1[0]==rec1[2] or rec1[1]==rec1[3] or rec2[0]==rec2[2] or rec2[1]==rec2[3]:
            return False
        if rec2[0] >= rec1[2] or rec2[2] <= rec1[0] or rec2[1] >= rec1[3] or rec2[3] <= rec1[1]: 
            return False
        return True