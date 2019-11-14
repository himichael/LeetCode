class Solution(object):
	def findAnagrams(self, s, p):
		"""
		:type s: str
		:type p: str
		:rtype: List[int]
		"""
		if not (s and p):
			return []
		left,right = 0,0
		s_len,p_len = len(s),len(p)
		p_dict,window = dict(),dict()
		res = []
		for i in p:
			p_dict[i] = p_dict.get(i,0)+1
		while right<s_len:
			c = s[right]
			if c not in p_dict:
				window.clear()
				right += 1
				left = right
			else:
				window[c] = window.get(c,0)+1
				if (right-left+1)==p_len:
					if window==p_dict:
						res.append(left)
					window[s[left]] -= 1
					left += 1
				right += 1
		return res