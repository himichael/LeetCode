class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(s==None or len(s)==0):
            return 0
        stack = [-1]
        res = 0
        for i in range(len(s)):
            if(s[i] == '('):
                stack.append(i)
            else:
                stack.pop()
                if(not stack):
                    stack.append(i)
                else:
                    res = max(i-stack[len(stack)-1], res)
        return res