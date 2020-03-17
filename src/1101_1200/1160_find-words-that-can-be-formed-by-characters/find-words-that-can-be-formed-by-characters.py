class Solution(object):
	def countCharacters(self, words, chars):
		"""
		:type words: List[str]
		:type chars: str
		:rtype: int
		"""
		if not (words and chars):
			return 0
		res = 0
		d = dict()
		for c in chars:
			if c not in d:
				d[c] = 1
			else:
				d[c] += 1
		for word in words:
			tmp = dict(d)
			is_ok = True
			for c in word:
				if c in tmp:
					tmp[c] -= 1
					if tmp[c]==0:
						del tmp[c]
				else:
					is_ok = False
					break
			if is_ok:
				res += len(word)
		return res