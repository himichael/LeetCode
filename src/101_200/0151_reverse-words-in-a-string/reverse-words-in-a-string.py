class Solution(object):
	def reverseWords(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		return " ".join(s.split()[::-1])
		
		
		
	# 自己实现，去头尾空格，反转字符串，再反转每个单词
	def reverseWords(self, s):
		if not s:
			return s
		def trim_space(s):
			left = 0
			right = len(s)-1
			while left<=right and s[left]==" ":
				left += 1
			while left<right and s[right]==" ":
				right -= 1
			output = []
			while left<=right:
				if s[left]!=" ":
					output.append(s[left])
				elif output and output[-1]!=" ":
					output.append(s[left])
				left += 1
			return output
		
		def reverse(arr,left,right):
			while left<right:
				arr[left],arr[right] = arr[right],arr[left]
				left,right = left+1,right-1
		
		def reverse_each_word(arr):
			n = len(arr)
			left,right = 0,0
			while left<n:
				while right<n and  arr[right]!=" ":
					right += 1
				reverse(arr,left,right-1)
				left = right+1
				right += 1
		
		arr = trim_space(s)
		reverse(arr,0,len(arr)-1)
		reverse_each_word(arr)
		return "".join(arr)