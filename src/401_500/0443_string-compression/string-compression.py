class Solution(object):
	def compress(self, chars):
		start = 0
		write = 0
		n = len(chars)
		for read,c in enumerate(chars):
			if read+1==n or chars[read+1]!=c:
				chars[write] = chars[start]
				write += 1
				if read>start:
					for digit in str(read-start+1):
						chars[write] = digit
						write += 1
				start = read + 1
		return write