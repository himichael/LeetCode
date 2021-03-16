class Solution(object):
	def isMatch(self, text, pattern):
		"""
		:type s: str
		:type p: str
		:rtype: bool
		"""
		if(not pattern):
			return not text
		first_match = bool(text) and (pattern[0]==text[0] or pattern[0]=='.')
		if( len(pattern)>=2 and pattern[1]=='*'):
			return self.isMatch(text,pattern[2:]) or (first_match and self.isMatch(text[1:],pattern))
		else:
			return first_match and self.isMatch(text[1:],pattern[1:])
			
			
	# 递归 + 记忆化，可以AC
	# 如果使用字符串截取的方式，比如s[1:],p[1:]这种就会超时，必须用i,j下标的方式
    def isMatch(self, s, p):
        mem = {}
        n = len(s)
        m = len(p)
        def f(i,j):
            if (i,j) in mem:
                return mem[i,j]
            if i == n:
                return j == m or (p[j] == "*" and f(i, j + 1))
            if j == m:
                return False
            if p[j] == "*":
                res =  f(i + 1, j) or f(i, j + 1)
            else:
                first = i < n and p[j] in (s[i], "?")
                res = first and f(i + 1, j + 1)
            mem[i,j] = res
            return mem[i,j]
        return f(0, 0)