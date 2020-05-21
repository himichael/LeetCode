class Solution(object):
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""	
		if not s or len(s)==0:
			return ""
		def expand_center(left,right):
			L,R = left,right
			while L>=0 and R<len(s) and s[L]==s[R]:
				L -= 1
				R += 1
			return R-L-1
		start,end = 0,0
		for i in xrange(len(s)):
			odd = expand_center(i,i)
			even = expand_center(i,i+1)
			max_len = max(odd,even)
			if max_len>(end-start):
				start = i-(max_len-1)/2
				end = i+1+(max_len)/2
		return s[start:end]
		
		
		
	# 暴力解法(超时)
	def longestPalindrome(self, s):	
		if not s or len(s)<2:
			return s
		N = len(s)
		max_len = 0
		left,right = 0,0
		def valid(begin,end):
			size = 0
			while begin<end:
				if s[begin]==s[end]:
					begin += 1
					end -= 1
				else:
					return False
			return True
		for j in xrange(0,N):
			for i in xrange(j+1):
				if valid(i,j) and j-i+1>max_len:
					max_len = j-i+1
					left = i
					right = j+1
		return s[left:right]

		
		
	# 另一种中心扩展实现，好理解一些
	def longestPalindrome(self, s):
		if not s:
			return s
		n = len(s)
		def expand(i,j):
			while i>=0 and j<n and s[i]==s[j]:
				i -= 1
				j += 1
			return i+1,j-1
		begin = 0
		end = 0
		for i in xrange(n):
			left1,right1 = expand(i,i)
			left2,right2 = expand(i,i+1)
			if right1-left1>(end-begin):
				begin = left1
				end = right1
			if right2-left2>(end-begin):
				begin = left2
				end = right2
		return s[begin:end+1]
		
		
		