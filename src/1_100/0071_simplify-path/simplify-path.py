class Solution(object):
    def simplifyPath(self, path):
        if not path:
            return ""
        stack = []
        arr = path.split("/")
        for i in arr:
            if i == "":
                continue
            elif i == '.':
                continue
            elif i == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(i)      
        res = ""
        for i in stack:
            res += "/" + i
        if not res:
            return "/"
        return res