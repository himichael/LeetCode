class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if(n == 0):
            return []
        res = []
        def recursion(left,right,content):
            if(left==n and right==n):
                res.append(content)
                return
            if(left>n or right>n or left<right):
                return
            recursion(left+1, right, content+"(")
            recursion(left, right+1, content+")")
        recursion(0, 0, "")
        return res
		
    def generateParenthesis_2(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def recursion(left,right,content):
            print "left->"+str(left)+"  right->"+str(right)+" content->"+content
            if(left==n and right==n):
                res.append(content)
                return
            if(left < n):
                recursion(left+1, right, content+"(")
            if(left>right and right<n):
                recursion(left, right+1, content+")")
        recursion(0,0,"")
        return res