class Solution(object):
    def removeKdigits(self, num, k):
        stack = []
        remain = len(num) - k
        for i in num:
            while k>0 and stack and stack[-1]>i:
                stack.pop()
                k -= 1
            stack.append(i)
        return "".join(stack[:remain]).lstrip("0") or '0'
