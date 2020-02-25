class Solution(object):
	def convert(self, s, numRows):
		if not s or numRows<=1:
			return s
		n = len(s)		
		res = [[] for _ in xrange(min(n,numRows))]	
		is_going_down = False
		j = 0
		ans = ""
		for c in s:
			res[j].append(c)
			if j==0 or j==numRows-1:
				is_going_down = not is_going_down
			j = j+1 if is_going_down else j-1
		for i in res:
			ans += "".join(i)
		return ans