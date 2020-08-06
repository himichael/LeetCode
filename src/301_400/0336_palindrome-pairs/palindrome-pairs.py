class Solution:
	def palindromePairs(self, words):
		n = len(words)
		indices = {word[::-1]: i for i, word in enumerate(words)}
		def findWord(s, left, right):
			return indices.get(s[left:right+1], -1)
        
		def isPalindrome(s, left, right):
			size = right - left + 1
			for i in xrange(0,size//2):
				if s[left+i]!=s[right-i]:
					return False
			return True
        
		ret = list()
		for i, word in enumerate(words):
			m = len(word)
			for j in range(m + 1):
				if isPalindrome(word, j, m - 1):
					leftId = findWord(word, 0, j - 1)
					if leftId != -1 and leftId != i:
						ret.append([i, leftId])
				if j and isPalindrome(word, 0, j - 1):
					rightId = findWord(word, j, m - 1)
					if rightId != -1 and rightId != i:
						ret.append([rightId, i])
		return ret